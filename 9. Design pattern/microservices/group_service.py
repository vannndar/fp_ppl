from database import MongoDB

class GroupService:
    def __init__(self):
        self.db = MongoDB()

    def create_group(self, group_id, group_name, owner_id):
        if self.db.get_group(group_id):
            print(f"[GroupService] Group {group_id} already exists")
            return False
        group_data = {
            "name": group_name,
            "owner": owner_id,
            "members": [owner_id],
            "tasks": []
        }
        self.db.save_group(group_id, group_data)
        print(f"[GroupService] Group created: {group_id}")
        return True

    def join_group(self, group_id, user_id):
        self.db.add_member(group_id, user_id)

    def get_group_members(self, group_id):
        group = self.db.get_group(group_id)
        if group:
            return group.get("members", [])
        return []