import pydantic


class User(pydantic.BaseModel):
    id: int
    username: str
    email: str
