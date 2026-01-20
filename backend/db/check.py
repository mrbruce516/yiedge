from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core import PydanticCustomError
import re

class SignupForm(BaseModel):
    name: str
    email: EmailStr
    phone: str

    # 电话校验
    @field_validator("phone")
    def validate_jp_phone(cls, v):
        pattern = r"^0[789]0[-]?\d{4}[-]?\d{4}$"
        if not re.match(pattern, v):
            raise PydanticCustomError(
                "phone_invalid",
                "電話番号の形式が正しくありません"
            )
        return v