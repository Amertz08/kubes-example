import sqlalchemy.orm

import schemas

mapper_registry = sqlalchemy.orm.registry()

users = sqlalchemy.Table(
    "users",
    mapper_registry.metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
)


def start_mappers():
    mapper_registry.map_imperatively(schemas.User, users)
