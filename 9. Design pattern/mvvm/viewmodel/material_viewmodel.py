from common.event import Observable

class MaterialViewModel(Observable):
    def __init__(self, db_client):
        super().__init__()
        self.db = db_client
        self.material = None

    def load_material(self, material_id):
        self.material = self.db.get_material(material_id)
        self.notify(self.material)

    def update_material(self, material_id, data):
        self.db.save_material(material_id, data)
        self.material = data
        self.notify(self.material)
