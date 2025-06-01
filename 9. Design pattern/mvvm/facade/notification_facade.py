class NotificationFacade:
    def send_notification(self, user_id, title, message):
        print(f"[NotificationFacade] Sending notification to {user_id}: {title} - {message}")
