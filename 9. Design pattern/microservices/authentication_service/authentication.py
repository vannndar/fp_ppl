from common.event_bus import event_bus
import hashlib
import os
import datetime
import jwt
class AuthenticationService:
    def __init__(self, db):
        self.db = db  # Instance PostgreSQL

    def register_user(self, user_id, user_data):
        """ Register a new user with hashed password and registration timestamp """
        if self.db.get_user(user_id):
            print(f"[AuthenticationService] User {user_id} already exists")
            return False
        # Hash the password for security
        hashed_password = self.hash_password(user_data['password'])
        user_data['password'] = hashed_password

        # Add registration timestamp
        user_data['registered_at'] = datetime.datetime.now().isoformat()

        # Save user data to the database
        self.db.save_user(user_id, user_data)
        print(f"[AuthenticationService] User registered: {user_id}")
        return True

    def hash_password(self, password):
        """ Hash the password with a salt for extra security """
        salt = os.urandom(32) 
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password 

    def authenticate(self, user_id, password):
        """ Authenticate a user by checking the hashed password """
        user = self.db.get_user(user_id)
        if user:
            # Hash the provided password and compare with stored hash
            stored_salt = user['password'][:32]
            stored_hash = user['password'][32:]
            
            # Hash the entered password with the stored salt and compare
            entered_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)
            if entered_hash == stored_hash:
                print(f"[AuthenticationService] User {user_id} authenticated")
                return self.generate_jwt(user_id)
            else:
                print(f"[AuthenticationService] Authentication failed for user {user_id}")
                return None
        print(f"[AuthenticationService] User {user_id} not found")
        return None

    def generate_jwt(self, user_id):
        """ Generate JWT token """
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        secret_key = "secret"  # In a real app, store this securely
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token

    def verify_jwt(self, token):
        """ Verify JWT token """
        secret_key = "secret"
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return None
        except jwt.InvalidTokenError:
            print("Invalid token")
            return None