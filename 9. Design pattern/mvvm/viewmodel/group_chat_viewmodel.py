from common.event import Observable

class GroupChatViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.message = None

    def load_message(self, message_id):
        self.message = self.db.get_message(message_id)
        self.notify(self.message)

    def send_message(self, message_id, data):
        self.db.save_message(message_id, data)
        self.message = data
        self.notify(self.message)
