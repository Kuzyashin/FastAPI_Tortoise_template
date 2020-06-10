import uuid
from datetime import datetime
from typing import Optional, TypeVar

from pydantic import BaseModel, EmailStr, UUID4, validator


class BaseProperties(BaseModel):
    @validator("hashed_id", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()

    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={"id", "is_superuser", "is_active"},
        )

    def create_update_dict_superuser(self):
        return self.dict(exclude_unset=True, exclude={"id"})


class BaseUser(BaseProperties):
    first_name: Optional[str]
    last_name: Optional[str]
    hashed_id: Optional[UUID4] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    created_at: Optional[datetime]


class BaseUserCreate(BaseProperties):
    first_name: Optional[str]
    last_name: Optional[str]
    hashed_id: Optional[UUID4] = None
    email: EmailStr
    username: Optional[str]
    password: str


class BaseUserUpdate(BaseProperties):
    first_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]
    username: Optional[str]


class BaseUserDB(BaseUser):
    id: int
    hashed_id: UUID4
    password_hash: str
    updated_at: datetime
    last_login: Optional[datetime]

    class Config:
        orm_mode = True


class BaseUserOut(BaseUser):
    id: int

    class Config:
        orm_mode = True
