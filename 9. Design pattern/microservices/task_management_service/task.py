class Task:
    def __init__(self, task_id, task_data):
        self.task_id = task_id
        self.task_data = task_data
        self.state = PendingState()  # Initial state is Pending
    
    def set_state(self, state):
        self.state = state
    
    def perform_action(self):
        self.state.perform_action(self)

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