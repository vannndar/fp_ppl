class ApiGateway:
    def __init__(self, auth_service, group_service, messaging_service, reminder_service, notification_service):
        self.auth_service = auth_service
        self.group_service = group_service
        self.messaging_service = messaging_service
        self.reminder_service = reminder_service
        self.notification_service = notification_service

    def register_user(self, user_id, user_data):
        return self.auth_service.register_user(user_id, user_data)

    def authenticate_user(self, user_id):
        return self.auth_service.authenticate(user_id)

    def create_group(self, group_id, group_name, owner_id):
        return self.group_service.create_group(group_id, group_name, owner_id)

    def join_group(self, group_id, user_id):
        self.group_service.join_group(group_id, user_id)

    def send_group_message(self, group_id, user_id, content):
        self.messaging_service.send_message(group_id, user_id, content)

    def set_reminder(self, user_id, reminder_text):
        self.reminder_service.set_reminder(user_id, reminder_text)
