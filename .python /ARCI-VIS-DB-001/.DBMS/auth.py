import socket
import pickle
class auth: 
    def __init__(self) -> None:
        self.start = True 
        self.running = True 
        self.db_unit = ".internal_DB"
    def __del__(self) -> None:
        self.start = False
        self.running = False
        self.db_unit = None
    def auth(self,hostname, username, password):
        with open('auth.data.bin','rb') as auth_file:
            user_admin_data = pickle.load(auth_file)
            del auth_file
        if user_admin_data['hostname'] == hostname and user_admin_data['username'] == username and user_admin_data['password'] == password:
            return True
        else:
            return False



