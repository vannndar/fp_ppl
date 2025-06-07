from common.event_bus import event_bus
from task_management_service.task import Task
import jwt

class TaskManagementService:
    def __init__(self, mongo_db):
        self.mongo_db = mongo_db  # Instance MongoDB]
    
    def verify_jwt(self, token):
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return None
        except jwt.InvalidTokenError:
            print("Invalid token")
            return None

    def create_task(self, task_id, task_data, group_id):
        if not self.mongo_db.get_group(group_id):
            print(f"[TaskManagementService] Group {group_id} not found")
            return False
        if self.mongo_db.get_task(task_id):
            print(f"[TaskManagementService] Task {task_id} already exists")
            return False
        task = Task(task_id, task_data, group_id)  
        self.mongo_db.save_task(task)
        print(f"[TaskManagementService] Task created: {task_id}")
        event_bus.publish("TaskCreated", {"task_id": task_id, "data": task_data, "group_id": group_id})
        return task
    
    def get_task_by_group(self, group_id):
        task = self.mongo_db.get_tasks(group_id)
        if not task:
            print(f"[TaskManagementService] Task in {group_id} not found")
            return None
        print(f"[TaskManagementService] Retrieved task: {task}")
        return task

    def set_reminder(self, task_id, reminder_data):
        task = self.mongo_db.get_task(task_id)
        if not task:
            print(f"[TaskManagementService] Task {task_id} not found")
            return False
        task.set_reminder(reminder_data.get('reminder_time'))
        self.mongo_db.update_task(task_id, task)
        print(f"[TaskManagementService] Reminder set for task {task_id}")
        event_bus.publish("ReminderSet", {"task_id": task_id, "reminder": reminder_data, "group_id": task.group_id})
        return True

    def schedule_event(self, schedule_id, schedule_data, group_id):
        if self.mongo_db.get_schedule(schedule_id):
            print(f"[TaskManagementService] Schedule {schedule_id} already exists")
            return False
        if not self.mongo_db.get_group(group_id):
            print(f"[TaskManagementService] Group {group_id} not found")
            return False
        schedule_data['group_id'] = group_id
        self.mongo_db.create_schedule(schedule_id, schedule_data)
        print(f"[TaskManagementService] Schedule created: {schedule_id}")
        event_bus.publish("ScheduleCreated", {"schedule_id": schedule_id, "data": schedule_data, "group_id": group_id})
        return True
    
    def get_schedule_by_group(self, group_id):
        schedules = self.mongo_db.get_schedule_by_group(group_id)
        if not schedules:
            print(f"[TaskManagementService] No schedules found for group {group_id}")
            return []
        print(f"[TaskManagementService] Retrieved schedules for group {group_id}")
        return schedules

    def start_task(self, task):
        task.set_state("in_progress")
    
    def complete_task(self, task):
        task.set_state("completed")