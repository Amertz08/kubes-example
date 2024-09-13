import sqlalchemy

import schemas


class UserRepository:
    def __init__(self, url):
        self.engine = sqlalchemy.create_engine(url)

    def __call__(self):
        return self

    def add(self, username: str, email: str):
        with self.engine.connect() as conn:
            result = conn.execute(
                sqlalchemy.insert(schemas.User)
                .values(username=username, email=email)
                .returning(sqlalchemy.literal_column("*"))
            ).fetchone()
        return schemas.User.model_validate(
            dict(id=result.id, username=result.username, email=result.email)
        )

    def get(self, user_id: int) -> schemas.User | None:
        with self.engine.connect() as conn:
            result = conn.execute(
                sqlalchemy.select(schemas.User).where(id=user_id)
            ).fetchone()
            return schemas.User.model_validate(
                dict(id=result.id, username=result.username, email=result.email)
            )
