from common.database import PostgreSQL, MongoDB, FirebaseRealtimeDB, FirebaseStorage, FCMClient
from common.event_bus import EventBus, event_bus
from common.api_gateway import ApiGateway
from authentication_service.authentication import AuthenticationService
from group_messaging_service.group_messaging import GroupMessagingService
from task_management_service.task_management import TaskManagementService
from content_notes_service.content_notes import ContentNotesService
from notification_service.notification import NotificationService

def main():
    # Inisialisasi database simulasi
    pg_db = PostgreSQL()
    mongo_db = MongoDB()
    firebase_db = FirebaseRealtimeDB()
    firebase_storage = FirebaseStorage()
    fcm_client = FCMClient()

    # Inisialisasi service
    auth_service = AuthenticationService(pg_db)
    group_service = GroupMessagingService(mongo_db, firebase_db)
    task_service = TaskManagementService(mongo_db)
    content_service = ContentNotesService(firebase_storage)
    notification_service = NotificationService(fcm_client)

    # Facade / API Gateway
    api_gateway = ApiGateway(auth_service, group_service, task_service, content_service, notification_service)

    # Contoh operasi
    print("--- Starting microservices simulation... ---\n")
    api_gateway.register_user("user1", {"name": "Alice", "password": "password123"})
    api_gateway.register_user("user2", {"name": "Bob", "password": "password456"})
    api_gateway.register_user("user3", {"name": "Charlie", "password": "password789"})

    tokenUser1 = api_gateway.authenticate("user1", "password123")
    tokenUser2 = api_gateway.authenticate("user2", "password456")

    print("\n--- Group Messaging Operations ---\n")
    api_gateway.create_group("group1", "Study Group", tokenUser1)
    api_gateway.send_message("group1", {"sender": tokenUser1, "text": "Hello, team!"})
    api_gateway.join_group("group1", tokenUser2)
    api_gateway.send_message("group1", {"sender": tokenUser2, "text": "Hi Alice!"})
    api_gateway.send_message("group1", {"sender": tokenUser1, "text": "Let's meet tomorrow."})
    api_gateway.send_message("group1", {"sender": tokenUser2, "text": "Sure, sounds good!"})
    message = api_gateway.get_messages("group1")
    print(f"[Main] Messages in group1: {message}")

    print("\n--- Task Management Operations ---\n")
    task = api_gateway.create_task("task1", {"title": "Math Homework", "due_date": "2025-06-10"}, "group1")
    task = api_gateway.create_task("task2", {"title": "Science Project", "due_date": "2025-06-15"}, "group1")
    api_gateway.set_reminder("task1", {"reminder_time": "2025-06-09T18:00"})
    api_gateway.schedule_event("schedule1", {"event": "Group Meeting", "time": "2025-06-11T15:00"}, "group1")
    api_gateway.start_task(task)
    tasks = api_gateway.get_task_by_group("group1")
    api_gateway.complete_task(task)
    schedule = api_gateway.get_schedule_by_group("group1")
    print(f"[Main] Schedule for group1: {schedule}")
    schedule = api_gateway.get_schedule_by_group("group2")
    print(f"[Main] Schedule for group2: {schedule}")

    print("\n--- Content Notes Operations ---\n")
    api_gateway.upload_content("content1", {"title": "Calculus Notes", "file_url": "http://example.com/calculus.pdf"}, "group1")
    api_gateway.edit_content("content1", {"title": "Calculus Notes Updated", "file_url": "http://example.com/calculus_v2.pdf"})

if __name__ == "__main__":
    main()
