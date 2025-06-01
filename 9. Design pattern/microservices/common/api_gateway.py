class ApiGateway:
    def __init__(self, auth_service, group_service, task_service, content_service, notification_service):
        self.auth_service = auth_service
        self.group_service = group_service
        self.task_service = task_service
        self.content_service = content_service
        self.notification_service = notification_service

    # Authentication API
    def register_user(self, user_id, user_data):
        print("[ApiGateway] register_user")
        return self.auth_service.register_user(user_id, user_data)

    def authenticate(self, user_id):
        print("[ApiGateway] authenticate")
        return self.auth_service.authenticate(user_id)

    # Group API
    def create_group(self, group_id, group_name, owner_id):
        print("[ApiGateway] create_group")
        return self.group_service.create_group(group_id, group_name, owner_id)

    def send_message(self, group_id, message):
        print("[ApiGateway] send_message")
        return self.group_service.send_message(group_id, message)

    def join_group(self, group_id, user_id):
        print("[ApiGateway] join_group")
        return self.group_service.join_group(group_id, user_id)

    # Task API
    def create_task(self, task_id, task_data):
        print("[ApiGateway] create_task")
        return self.task_service.create_task(task_id, task_data)

    def set_reminder(self, task_id, reminder_data):
        print("[ApiGateway] set_reminder")
        return self.task_service.set_reminder(task_id, reminder_data)

    def schedule_event(self, schedule_id, schedule_data):
        print("[ApiGateway] schedule_event")
        return self.task_service.schedule_event(schedule_id, schedule_data)

    # Content API
    def upload_content(self, content_id, content_data):
        print("[ApiGateway] upload_content")
        return self.content_service.upload_content(content_id, content_data)

    def edit_content(self, content_id, new_data):
        print("[ApiGateway] edit_content")
        return self.content_service.edit_content(content_id, new_data)
