from common.event_bus import event_bus

class TaskManagementService:
    def __init__(self, mongo_db):
        self.mongo_db = mongo_db  # Instance MongoDB

    def create_task(self, task_id, task_data):
        if self.mongo_db.get_group(task_id):
            print(f"[TaskManagementService] Task {task_id} already exists")
            return False
        self.mongo_db.save_group(task_id, task_data)  # Reuse MongoDB for tasks collection
        print(f"[TaskManagementService] Task created: {task_id}")
        event_bus.publish("TaskCreated", {"task_id": task_id, "data": task_data})
        return True

    def set_reminder(self, task_id, reminder_data):
        task = self.mongo_db.get_group(task_id)
        if not task:
            print(f"[TaskManagementService] Task {task_id} not found")
            return False
        task["reminder"] = reminder_data
        self.mongo_db.save_group(task_id, task)
        print(f"[TaskManagementService] Reminder set for task {task_id}")
        event_bus.publish("ReminderSet", {"task_id": task_id, "reminder": reminder_data})
        return True

    def schedule_event(self, schedule_id, schedule_data):
        if self.mongo_db.get_group(schedule_id):
            print(f"[TaskManagementService] Schedule {schedule_id} already exists")
            return False
        self.mongo_db.save_group(schedule_id, schedule_data)
        print(f"[TaskManagementService] Schedule created: {schedule_id}")
        event_bus.publish("ScheduleCreated", {"schedule_id": schedule_id, "data": schedule_data})
        return True
