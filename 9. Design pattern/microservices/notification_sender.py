class NotificationSender:
    def send_notification(self, user_id: str, message: str):
        raise NotImplementedError

class FcmSender(NotificationSender):
    def send_notification(self, user_id: str, message: str):
        print(f"[FCM] Push notification to {user_id}: {message}")

class EmailSender(NotificationSender):
    def send_notification(self, user_id: str, message: str):
        print(f"[Email] Sending email to {user_id}: {message}")
