from common.event import Observable

class ReminderViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.reminder = None

    def load_reminder(self, reminder_id):
        self.reminder = self.db.get_reminder(reminder_id)
        self.notify(self.reminder)

    def update_reminder(self, reminder_id, data):
        self.db.save_reminder(reminder_id, data)
        self.reminder = data
        self.notify(self.reminder)
