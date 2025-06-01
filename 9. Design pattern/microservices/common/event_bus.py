class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        self.subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event_type, data):
        handlers = self.subscribers.get(event_type, [])
        for handler in handlers:
            handler(data)

event_bus = EventBus()
