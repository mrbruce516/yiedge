from pydantic import BaseModel, EmailStr

class SignupForm(BaseModel):
    name: str
    email: EmailStr
    phone: str