from common.event import Observable

class GroupViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.group = None

    def load_group(self, group_id):
        self.group = self.db.get_group(group_id)
        self.notify(self.group)

    def update_group(self, group_id, data):
        self.db.save_group(group_id, data)
        self.group = data
        self.notify(self.group)
