from notification_sender import NotificationSender

class NotificationService:
    def __init__(self, event_bus, senders: list[NotificationSender]):
        self.event_bus = event_bus
        self.senders = senders
        self.event_bus.subscribe("MessageSent", self.on_message_sent)
        self.event_bus.subscribe("ReminderSet", self.on_reminder_set)

    def notify_all(self, user_id: str, message: str):
        for sender in self.senders:
            sender.send_notification(user_id, message)

    def on_message_sent(self, message):
        print(f"[NotificationService] Push notification for new message in group {message['group_id']}")
        user_id = message.get("user_id")
        content = f"New message in group {message['group_id']}: {message.get('content')}"
        if user_id:
            self.notify_all(user_id, content)

    def on_reminder_set(self, reminder):
        print(f"[NotificationService] Push notification for reminder: {reminder['text']} to user {reminder['user_id']}")
        user_id = reminder.get("user_id")
        content = f"Reminder: {reminder.get('text')}"
        if user_id:
            self.notify_all(user_id, content)
