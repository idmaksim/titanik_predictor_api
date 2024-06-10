from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    age: float = Field(default=1)
    p_class: int = Field(default=1)
    sex: int = Field(default=1)
    sibsp: int = Field(default=0)
    parch: int = Field(default=0)
