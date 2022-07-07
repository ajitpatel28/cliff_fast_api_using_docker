from pydantic import BaseModel, Field, EmailStr
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "cliff ai",
                "email": "ajit@cliff.ai",
                "password": "test"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "ajit@cliff.ai",
                "password": "test"
            }
        }
