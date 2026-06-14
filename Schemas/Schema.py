from pydantic import BaseModel, EmailStr, Field


class UserAddSchema(BaseModel):
    name: str = Field(max_length = 20, min_length = 5)
    password: str = Field(max_length = 20, min_length = 8)

class UserSchema(UserAddSchema):
    email: EmailStr

class UserDataSchema(BaseModel):
    pass

class NoticeSchema(BaseModel):
    title: str = Field(max_length = 60, min_length = 10)
    image: str = Field(max_length = 100, min_length = 3)



