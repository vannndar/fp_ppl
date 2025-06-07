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

    def authenticate(self, user_id, password):
        print("[ApiGateway] authenticate")
        return self.auth_service.authenticate(user_id, password)
    
    def verify_token(self, token):
        print("[ApiGateway] verify_token")
        return self.auth_service.verify_jwt(token)

    # Group API
    def create_group(self, group_id, group_name, ownerjwt):
        print("[ApiGateway] create_group")
        return self.group_service.create_group(group_id, group_name, ownerjwt)

    def send_message(self, group_id, message):
        print("[ApiGateway] send_message")
        return self.group_service.send_message(group_id, message)

    def get_messages(self, group_id):
        print("[ApiGateway] get_messages")
        return self.group_service.get_messages(group_id)

    def join_group(self, group_id, user_id):
        print("[ApiGateway] join_group")
        return self.group_service.join_group(group_id, user_id)

    # Task API
    def create_task(self, task_id, task_data, group_id):
        print("[ApiGateway] create_task")
        return self.task_service.create_task(task_id, task_data, group_id)

    def get_task_by_group(self, group_id):
        print("[ApiGateway] get_task")
        return self.task_service.get_task_by_group(group_id)

    def set_reminder(self, task_id, reminder_data):
        print("[ApiGateway] set_reminder")
        return self.task_service.set_reminder(task_id, reminder_data)

    def schedule_event(self, schedule_id, schedule_data, group_id):
        print("[ApiGateway] schedule_event")
        return self.task_service.schedule_event(schedule_id, schedule_data, group_id)

    def get_schedule_by_group(self, group_id):
        print("[ApiGateway] get_schedule")
        return self.task_service.get_schedule_by_group(group_id)
    
    def start_task(self, task):
        print("[ApiGateway] Starting task...")
        return self.task_service.start_task(task)

    def complete_task(self, task):
        print("[ApiGateway] Completing task...")
        return self.task_service.complete_task(task)

    # Content API
    def upload_content(self, content_id, content_data, group_id):
        print("[ApiGateway] upload_content")
        return self.content_service.upload_content(content_id, content_data, group_id)

    def edit_content(self, content_id, new_data):
        print("[ApiGateway] edit_content")
        return self.content_service.edit_content(content_id, new_data)

    def get_content(self, group_id):
        print("[ApiGateway] get_content")
        return self.content_service.get_content_by_group(group_id)