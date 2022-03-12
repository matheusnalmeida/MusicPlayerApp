from data.memory_database import MemoryDatabase
from models.user import User

class UserService:
    def __init__(self) -> None:
        self.database = MemoryDatabase.instance()

    def insert_user(self, user: User) -> User:
        if (user.is_valid()):
           self.database.users_table[user.id] = user 

    def get_user_by_username_pass(self, username: str, password: str) -> User:
        for id in self.database.users_table:
            user = self.database.users_table[id]
            if user.usuario == username and user.senha == password:
                return user