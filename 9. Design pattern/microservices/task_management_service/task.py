class Task:
    def __init__(self, task_id, task_data, group_id, reminder=None):
        self.task_id = task_id
        self.tittle = task_data.get('title')
        self.due_date = task_data.get('due_date')
        self.reminder = reminder
        self.group_id = group_id
        self.reminder = reminder
        self.state = PendingState()  # Initial state is Pending
    
    def set_state(self, state):
        self.state = state
    
    def perform_action(self):
        self.state.perform_action(self)
    
    def set_reminder(self, reminder):
        self.reminder = reminder
        print(f"[Task] Reminder set for task {self.task_id}: {reminder}")
    
    def set_state(self, state):
        if state == "in_progress":
            self.state = InProgressState()
        elif state == "completed":
            self.state = CompletedState()
        print(f"[Task] State changed to {self.state.__class__.__name__} for task {self.task_id}")
    
    def __str__(self):
        return f"Task(id={self.task_id}, title={self.tittle}, due_date={self.due_date}, reminder={self.reminder}, group_id={self.group_id}, state={self.state.__class__.__name__})"
    
    def __repr__(self):
        return self.__str__()

class TaskState:
    def perform_action(self, task):
        pass

class PendingState(TaskState):
    def perform_action(self, task):
        print(f"[Task] Task {task.task_id} is pending.")
        task.set_state(InProgressState())
        
class InProgressState(TaskState):
    def perform_action(self, task):
        print(f"[Task] Task {task.task_id} is in progress.")
        
class CompletedState(TaskState):
    def perform_action(self, task):
        print(f"[Task] Task {task.task_id} is completed.")