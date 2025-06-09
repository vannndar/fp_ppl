from common.event_bus import event_bus

class NotificationService:
    def __init__(self, fcm_client):
        self.fcm_client = fcm_client
        event_bus.subscribe("MessageSent", self.on_message_sent)
        event_bus.subscribe("TaskCreated", self.on_task_created)
        event_bus.subscribe("ReminderSet", self.on_reminder_set)
        event_bus.subscribe("ScheduleCreated", self.on_schedule_created)
        event_bus.subscribe("ContentUploaded", self.on_content_uploaded)
        event_bus.subscribe("ContentUpdated", self.on_content_updated)

    def on_message_sent(self, event_data):
        print(f"[NotificationService] Notify message in group {event_data['group_id']}")
        self.fcm_client.send_push(event_data['group_id'], "New Message", f"New message in group {event_data['group_id']}")

    def on_task_created(self, event_data):
        print(f"[NotificationService] Notify task created {event_data['task_id']}")
        self.fcm_client.send_push(event_data['group_id'], "New Task", f"Task created: {event_data['task_id']}")

    def on_reminder_set(self, event_data):
        print(f"[NotificationService] Notify reminder set {event_data['task_id']}")
        self.fcm_client.send_push(event_data['group_id'], "Reminder Set", f"Reminder set for task {event_data['task_id']}")

    def on_schedule_created(self, event_data):
        print(f"[NotificationService] Notify schedule created {event_data['schedule_id']}")
        self.fcm_client.send_push(event_data['group_id'], "Schedule Created", f"Schedule created: {event_data['schedule_id']}")

    def on_content_uploaded(self, event_data):
        print(f"[NotificationService] Notify content uploaded {event_data['content_id']}")
        self.fcm_client.send_push(event_data['group_id'], "Content Uploaded", f"Content uploaded: {event_data['content_id']}")

    def on_content_updated(self, event_data):
        print(f"[NotificationService] Notify content updated {event_data['content_id']}")
        self.fcm_client.send_push(event_data['group_id'], "Content Updated", f"Content updated: {event_data['content_id']}")
