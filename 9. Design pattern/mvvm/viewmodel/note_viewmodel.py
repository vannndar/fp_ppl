from common.event import Observable

class NoteViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.note = None

    def load_note(self, note_id):
        self.note = self.db.get_note(note_id)
        self.notify(self.note)

    def update_note(self, note_id, data):
        self.db.save_note(note_id, data)
        self.note = data
        self.notify(self.note)
