from typing import Union
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id: int, email: str, name: str):
        self.id = id
        self.email = email
        self.name = name

    def get_id(self):
        return str(self.id)

class FakeUserDatabase:
    users = {
        '1': User(1, 'alice@example.com', 'Alice'),
        '2': User(2, 'bob@example.com', 'Bob'),
        '3': User(3, 'carol@example.com', 'Carol')
    }

    def find(self, user_id:str) -> Union[User, None]:
        return self.users.get(user_id)
