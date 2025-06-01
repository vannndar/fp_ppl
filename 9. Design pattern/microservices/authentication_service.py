from database import PostgreSQL

class AuthenticationService:
    def __init__(self):
        self.db = PostgreSQL()

    def register_user(self, user_id, user_data):
        if self.db.get_user(user_id):
            print(f"[AuthenticationService] User {user_id} already exists")
            return False
        self.db.save_user(user_id, user_data)
        print(f"[AuthenticationService] User registered: {user_id}")
        return True

    def authenticate(self, user_id):
        user = self.db.get_user(user_id)
        if user:
            print(f"[AuthenticationService] User authenticated: {user_id}")
            return True
        print(f"[AuthenticationService] User not found: {user_id}")
        return False