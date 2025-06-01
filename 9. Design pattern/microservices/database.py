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

class FirebaseRealtimeDB:
    def __init__(self):
        self.messages = []

    def save_message(self, message):
        self.messages.append(message)
        print(f"[FirebaseRealtimeDB] Message saved: {message}")