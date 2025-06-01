from common.event import Observable

class UserViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.user = None

    def load_user(self, user_id):
        self.user = self.db.get_user(user_id)
        self.notify(self.user)

    def update_user(self, user_id, data):
        self.db.save_user(user_id, data)
        self.user = data
        self.notify(self.user)
