from common.event import Observable

class ScheduleViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.schedule = None

    def load_schedule(self, schedule_id):
        self.schedule = self.db.get_schedule(schedule_id)
        self.notify(self.schedule)

    def update_schedule(self, schedule_id, data):
        self.db.save_schedule(schedule_id, data)
        self.schedule = data
        self.notify(self.schedule)
