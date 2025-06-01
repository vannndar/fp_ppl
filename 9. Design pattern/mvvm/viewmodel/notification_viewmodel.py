class NotificationViewModel:
    def __init__(self, notification_facade):
        self.notification_facade = notification_facade

    def send_notification(self, user_id, title, message):
        self.notification_facade.send_notification(user_id, title, message)
