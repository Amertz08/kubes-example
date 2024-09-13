import schemas


class FakeUserRepo:
    def __init__(self):
        self.users = []

    def __call__(self):
        return self

    def add(self, username: str, email: str) -> schemas.User:
        _id = len(self.users) + 1
        user = schemas.User(id=_id, username=username, email=email)
        self.users.append(user)
        return user
