from event_bus import EventBus

class ReminderService:
    def __init__(self, event_bus: EventBus):
        self.reminders = {}
        self.event_bus = event_bus

    def set_reminder(self, user_id, reminder_text):
        self.reminders[user_id] = reminder_text
        print(f"[ReminderService] Reminder set for user {user_id}: {reminder_text}")
        self.event_bus.publish("ReminderSet", {"user_id": user_id, "text": reminder_text})

    def get_reminder(self, user_id):
        return self.reminders.get(user_id)