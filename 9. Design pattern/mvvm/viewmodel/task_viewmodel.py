from common.event import Observable

class TaskViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.task = None

    def load_task(self, task_id):
        self.task = self.db.get_task(task_id)
        self.notify(self.task)

    def update_task(self, task_id, data):
        self.db.save_task(task_id, data)
        self.task = data
        self.notify(self.task)
