# TODO: actually interact with the db
class UserRepository:
    def __init__(self, url):
        self.url = url

    def __call__(self):
        return self

    def add(self, username: str, email: str):
        return {"id": 1, "username": username, "email": email}
