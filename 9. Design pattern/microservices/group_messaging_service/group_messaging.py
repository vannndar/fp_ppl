from common.event_bus import event_bus

class GroupMessagingService:
    def __init__(self, mongo_db, firebase_db):
        self.mongo_db = mongo_db  # Instance MongoDB
        self.firebase_db = firebase_db  # Instance FirebaseRealtimeDB

    def create_group(self, group_id, group_name, owner_id):
        if self.mongo_db.get_group(group_id):
            print(f"[GroupMessagingService] Group {group_id} already exists")
            return False
        group_data = {
            "name": group_name,
            "owner": owner_id,
            "members": [owner_id],
            "messages": []
        }
        self.mongo_db.save_group(group_id, group_data)
        print(f"[GroupMessagingService] Group created: {group_id}")
        return True

    def send_message(self, group_id, message):
        group = self.mongo_db.get_group(group_id)
        if not group:
            print(f"[GroupMessagingService] Group {group_id} not found")
            return False
        # Simpan pesan ke Firebase Realtime DB
        self.firebase_db.save_message({"group_id": group_id, **message})
        print(f"[GroupMessagingService] Message sent to group {group_id}")
        event_bus.publish("MessageSent", {"group_id": group_id, "message": message})
        return True

    def get_messages(self, group_id):
        group = self.mongo_db.get_group(group_id)
        if not group:
            print(f"[GroupMessagingService] Group {group_id} not found")
            return []
        messages = self.firebase_db.get_messages(group_id)
        print(f"[GroupMessagingService] Retrieved messages for group {group_id}")
        return messages
    
    def join_group(self, group_id, user_id):
        group = self.mongo_db.get_group(group_id)
        if not group:
            print(f"[GroupMessagingService] Group {group_id} not found")
            return False
        if user_id in group["members"]:
            print(f"[GroupMessagingService] User {user_id} already in group {group_id}")
            return False
        group["members"].append(user_id)
        self.mongo_db.update_group(group_id, group)
        print(f"[GroupMessagingService] User {user_id} joined group {group_id}")
        return True
