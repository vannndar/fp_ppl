import datetime
class PostgreSQL:
    def __init__(self):
        self.users = {}

    def save_user(self, user_id, data):
        self.users[user_id] = data
        print(f"[PostgreSQL] User saved: {user_id}")

    def get_user(self, user_id):
        return self.users.get(user_id)

class MongoDB:
    def __init__(self):
        self.groups = {}
        self.tasks = {}
        self.schedules = {}

    def save_group(self, group_id, data):
        self.groups[group_id] = data
        print(f"[MongoDB] Group saved: {group_id}")

    def get_group(self, group_id):
        return self.groups.get(group_id)

    def add_member(self, group_id, user_id):
        group = self.groups.get(group_id)
        if group:
            if user_id not in group["members"]:
                group["members"].append(user_id)
                print(f"[MongoDB] User {user_id} joined group {group_id}")
            else:
                print(f"[MongoDB] User {user_id} already in group {group_id}")
            
    def update_group(self, group_id, data):
        if group_id in self.groups:
            self.groups[group_id] = data
            print(f"[MongoDB] Group updated: {group_id}")
        else:
            print(f"[MongoDB] Group {group_id} not found")

    def save_task(self, task):
        self.tasks[task.task_id] = task
        print(f"[MongoDB] Task saved: {task.task_id}")

    def get_tasks(self, group_id):
        tasks = [task for task in self.tasks.values() if task.group_id == group_id]
        return tasks
    
    def get_task(self, task_id):
        return self.tasks.get(task_id)
    
    def update_task(self, task_id, task):
        if task_id in self.tasks:
            self.tasks[task_id] = task
            print(f"[MongoDB] Task updated: {task_id}")
        else:
            print(f"[MongoDB] Task {task_id} not found")
    
    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"[MongoDB] Task deleted: {task_id}")
        else:
            print(f"[MongoDB] Task {task_id} not found")
    
    def create_schedule(self, schedule_id, schedule_data):
        if schedule_id in self.schedules:
            print(f"[MongoDB] Schedule {schedule_id} already exists")
            return False
        self.schedules[schedule_id] = schedule_data
        print(f"[MongoDB] Schedule created: {schedule_id}")
        return True
    
    def get_schedule(self, schedule_id):
        return self.schedules.get(schedule_id)
    
    def get_schedule_by_group(self, group_id):
        return [schedule for schedule in self.schedules.values() if schedule.get("group_id") == group_id]

class FirebaseRealtimeDB:
    def __init__(self):
        self.messages = []

    def save_message(self, message):
        message["timestamp"] = datetime.datetime.utcnow().isoformat()
        self.messages.append(message)
        print(f"[FirebaseRealtimeDB] Message saved: {message}")

    def get_messages(self, group_id):
        return [msg for msg in self.messages if msg.get("group_id") == group_id]

class FirebaseStorage:
    def __init__(self):
        self.contents = {}

    def save_content(self, content_id, data):
        self.contents[content_id] = data
        print(f"[FirebaseStorage] Content saved: {content_id}")

    def get_content(self, content_id):
        return self.contents.get(content_id)

class FCMClient:
    def send_push(self, user_id, title, message):
        print(f"[FCM] Push to {user_id}: {title} - {message}")
