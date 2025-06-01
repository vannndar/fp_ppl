from common.event_bus import event_bus

class ContentNotesService:
    def __init__(self, firebase_storage):
        self.firebase_storage = firebase_storage  # Simulasi Firebase S3

    def upload_content(self, content_id, content_data):
        if self.firebase_storage.get_content(content_id):
            print(f"[ContentNotesService] Content {content_id} already exists")
            return False
        self.firebase_storage.save_content(content_id, content_data)
        print(f"[ContentNotesService] Content uploaded: {content_id}")
        event_bus.publish("ContentUploaded", {"content_id": content_id, "data": content_data})
        return True

    def edit_content(self, content_id, new_data):
        content = self.firebase_storage.get_content(content_id)
        if not content:
            print(f"[ContentNotesService] Content {content_id} not found")
            return False
        self.firebase_storage.save_content(content_id, new_data)
        print(f"[ContentNotesService] Content edited: {content_id}")
        event_bus.publish("ContentUpdated", {"content_id": content_id, "data": new_data})
        return True
