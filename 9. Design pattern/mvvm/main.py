from model.firebase_client import FirebaseClient
from viewmodel.user_viewmodel import UserViewModel
from viewmodel.group_viewmodel import GroupViewModel
from viewmodel.task_viewmodel import TaskViewModel
from viewmodel.reminder_viewmodel import ReminderViewModel
from viewmodel.schedule_viewmodel import ScheduleViewModel
from viewmodel.material_viewmodel import MaterialViewModel
from viewmodel.note_viewmodel import NoteViewModel
from viewmodel.group_chat_viewmodel import GroupChatViewModel
from viewmodel.notification_viewmodel import NotificationViewModel
from view.user_view import UserView
from view.group_view import GroupView
from view.task_view import TaskView
from view.reminder_view import ReminderView
from view.schedule_view import ScheduleView
from view.material_view import MaterialView
from view.note_view import NoteView
from view.group_chat_view import GroupChatView
from facade.notification_facade import NotificationFacade

def main():
    # Inisialisasi cloud db
    cloud_db = FirebaseClient()

    # Inisialisasi ViewModel dan View untuk User
    user_vm = UserViewModel(cloud_db)
    user_view = UserView()

    print("Inisialisasi ViewModel dan View untuk User...\n")
    # ViewModel subscribe ke View
    user_vm.subscribe(user_view)

    # Simulasi login dan update user
    user_vm.load_user("user1")  # Mengambil data user
    user_vm.update_user("user1", {"name": "Alice", "email": "alice@example.com"})  # Update data

    print("\n--- User data loaded and updated successfully. ---\n")
    # Inisialisasi ViewModel dan View untuk Group
    group_vm = GroupViewModel(cloud_db)
    group_view = GroupView()
    group_vm.subscribe(group_view)

    group_vm.load_group("group1")
    group_vm.update_group("group1", {"name": "Math Study Group", "members": ["user1"]})

    # Inisialisasi ViewModel dan View untuk Task
    print("\n--- Inisialisasi ViewModel dan View untuk Task...\n")
    task_vm = TaskViewModel(cloud_db)
    task_view = TaskView()
    task_vm.subscribe(task_view)

    task_vm.load_task("task1")
    task_vm.update_task("task1", {"title": "Finish Algebra Homework", "due_date": "2025-06-10"})

    # Inisialisasi ViewModel dan View untuk Reminder
    print("\n--- Inisialisasi ViewModel dan View untuk Reminder...\n")
    reminder_vm = ReminderViewModel(cloud_db)
    reminder_view = ReminderView()
    reminder_vm.subscribe(reminder_view)

    reminder_vm.load_reminder("reminder1")
    reminder_vm.update_reminder("reminder1", {"task_id": "task1", "time": "2025-06-09T18:00"})

    # Inisialisasi ViewModel dan View untuk Schedule
    print("\n--- Inisialisasi ViewModel dan View untuk Schedule...\n")
    schedule_vm = ScheduleViewModel(cloud_db)
    schedule_view = ScheduleView()
    schedule_vm.subscribe(schedule_view)

    schedule_vm.load_schedule("schedule1")
    schedule_vm.update_schedule("schedule1", {"event": "Final Exam", "time": "2025-06-15T09:00"})

    # Inisialisasi ViewModel dan View untuk Material
    print("\n--- Inisialisasi ViewModel dan View untuk Material...\n")
    material_vm = MaterialViewModel(cloud_db)
    material_view = MaterialView()
    material_vm.subscribe(material_view)

    material_vm.load_material("material1")
    material_vm.update_material("material1", {"title": "Calculus Notes", "url": "http://example.com/calculus.pdf"})

    # Inisialisasi ViewModel dan View untuk Note
    print("\n--- Inisialisasi ViewModel dan View untuk Note...\n")
    note_vm = NoteViewModel(cloud_db)
    note_view = NoteView()
    note_vm.subscribe(note_view)

    note_vm.load_note("note1")
    note_vm.update_note("note1", {"content": "Important calculus formulas", "tags": ["math", "exam"]})

    # Inisialisasi ViewModel dan View untuk GroupChat
    print("\n--- Inisialisasi ViewModel dan View untuk GroupChat...\n")
    chat_vm = GroupChatViewModel(cloud_db)
    chat_view = GroupChatView()
    chat_vm.subscribe(chat_view)

    chat_vm.load_message("msg1")
    chat_vm.send_message("msg2", {"sender": "user1", "text": "Hello, study group!"})

    # Notification Facade
    print("\n--- Inisialisasi Notification Facade...\n")
    notification_facade = NotificationFacade()
    notification_vm = NotificationViewModel(notification_facade)
    notification_vm.send_notification("user1", "Welcome", "Hello Alice, welcome to Study Buddy!")

if __name__ == "__main__":
    main()
