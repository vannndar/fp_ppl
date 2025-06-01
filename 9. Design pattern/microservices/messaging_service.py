from database import FirebaseRealtimeDB
from event_bus import EventBus

class MessagingService:
    def __init__(self, event_bus: EventBus):
        self.db = FirebaseRealtimeDB()
        self.event_bus = event_bus

    def send_message(self, group_id, user_id, content):
        message = {
            "group_id": group_id,
            "user_id": user_id,
            "content": content
        }
        self.db.save_message(message)
        self.event_bus.publish("MessageSent", message)