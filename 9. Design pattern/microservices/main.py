from authentication_service import AuthenticationService
from group_service import GroupService
from messaging_service import MessagingService
from reminder_service import ReminderService
from notification_service import NotificationService
from notification_sender import FcmSender, EmailSender
from event_bus import EventBus
from api_gateway import ApiGateway

def main():
    event_bus = EventBus()

    auth_service = AuthenticationService()
    group_service = GroupService()
    messaging_service = MessagingService(event_bus)
    reminder_service = ReminderService(event_bus)

    # Setup dua channel notifikasi sekaligus: Push dan Email
    fcm_sender = FcmSender()
    email_sender = EmailSender()
    notification_service = NotificationService(event_bus, [fcm_sender, email_sender])

    api_gateway = ApiGateway(auth_service, group_service, messaging_service, reminder_service, notification_service)

    # Contoh operasi melalui facade ApiGateway
    api_gateway.register_user("user1", {"name": "Alice"})
    api_gateway.authenticate_user("user1")
    api_gateway.create_group("group1", "Math Group", "user1")
    api_gateway.join_group("group1", "user1")
    api_gateway.send_group_message("group1", "user1", "Hello from multi-channel notification!")
    api_gateway.set_reminder("user1", "Exam tomorrow!")

    # Simulasi event untuk uji notifikasi multi channel
    event_bus.publish("MessageSent", {
        "group_id": "group1",
        "user_id": "user1",
        "content": "New group message for all channels!"
    })

    event_bus.publish("ReminderSet", {
        "user_id": "user1",
        "text": "This is a reminder sent on multiple channels."
    })

if __name__ == "__main__":
    main()
