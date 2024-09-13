import sqlalchemy

import tables


class UserRepository:
    def __init__(self, url):
        self.engine = sqlalchemy.create_engine(url)

    def __call__(self):
        return self

    def add(self, username: str, email: str):
        with self.engine.connect() as conn:
            # TODO: cannot commit transaction
            result = conn.execute(
                sqlalchemy.insert(tables.users)
                .values(username=username, email=email)
                .returning(sqlalchemy.literal_column("*"))
            )
            conn.commit()
        return {"id": 1, "username": username, "email": email}
