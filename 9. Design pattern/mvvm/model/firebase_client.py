class FirebaseClient:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.tasks = {}
        self.reminders = {}
        self.schedules = {}
        self.materials = {}
        self.notes = {}
        self.messages = {}

    # User
    def get_user(self, user_id):
        return self.users.get(user_id)

    def save_user(self, user_id, data):
        self.users[user_id] = data

    # Group
    def get_group(self, group_id):
        return self.groups.get(group_id)

    def save_group(self, group_id, data):
        self.groups[group_id] = data

    # Task
    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def save_task(self, task_id, data):
        self.tasks[task_id] = data

    # Reminder
    def get_reminder(self, reminder_id):
        return self.reminders.get(reminder_id)

    def save_reminder(self, reminder_id, data):
        self.reminders[reminder_id] = data

    # Schedule
    def get_schedule(self, schedule_id):
        return self.schedules.get(schedule_id)

    def save_schedule(self, schedule_id, data):
        self.schedules[schedule_id] = data

    # Material
    def get_material(self, material_id):
        return self.materials.get(material_id)

    def save_material(self, material_id, data):
        self.materials[material_id] = data

    # Note
    def get_note(self, note_id):
        return self.notes.get(note_id)

    def save_note(self, note_id, data):
        self.notes[note_id] = data

    # Message
    def get_message(self, message_id):
        return self.messages.get(message_id)

    def save_message(self, message_id, data):
        self.messages[message_id] = data
