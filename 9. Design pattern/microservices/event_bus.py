class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event_type, data):
        handlers = self.subscribers.get(event_type, [])
        print(f"[EventBus] Publishing event '{event_type}' with data: {data}")
        for handler in handlers:
            handler(data)