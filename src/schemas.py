import pydantic


class UserBase(pydantic.BaseModel):
    username: str
    email: str


class User(UserBase):
    id: int
