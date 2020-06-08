from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.applications.users.schemas import BaseUserDB, BaseUserCreate, BaseUserUpdate
from app.core.auth.schemas import CredentialsSchema
from app.core.base.base_models import BaseCreatedUpdatedAtModel, UUIDDBModel, BaseDBModel
from app.core.auth.utils import password
import logging
logger = logging.getLogger('AUTH')


class User(BaseDBModel, BaseCreatedUpdatedAtModel, UUIDDBModel):

    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    password_hash = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)

    def full_name(self) -> str:
        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()
        return self.username

    @classmethod
    async def get_by_email(cls, email: str) -> Optional[BaseUserDB]:
        try:
            query = cls.get(email=email)
            user = await query
            user_dict = await user.to_dict()

            return BaseUserDB(**user_dict)
        except DoesNotExist:
            return None

    @classmethod
    async def get_by_username(cls, username: str) -> Optional[BaseUserDB]:
        try:
            query = cls.get(username=username)
            user = await query
            user_dict = await user.to_dict()

            return BaseUserDB(**user_dict)
        except DoesNotExist:
            return None

    @classmethod
    async def create(cls, user: BaseUserCreate) -> BaseUserDB:
        user_dict = user.dict()
        password_hash = password.get_password_hash(password=user.password)
        model = cls(**user_dict, password_hash=password_hash)
        await model.save()
        user_dict = await model.to_dict()
        logger.info(user_dict)
        return BaseUserDB(**user_dict)

    @classmethod
    async def authenticate(cls, credentials: CredentialsSchema) -> Optional[BaseUserDB]:
        if credentials.email:
            user = await cls.get_by_email(credentials.email)
        elif credentials.username:
            user = await cls.get_by_username(credentials.username)
        else:
            return None

        if user is None:
            return None

        verified, updated_password_hash = password.verify_and_update_password(
            credentials.password, user.password_hash
        )

        logger.info(verified, updated_password_hash)

        if not verified:
            return None
        # Update password hash to a more robust one if needed
        if updated_password_hash is not None:
            user.password_hash = updated_password_hash
            await cls.update(user)
        return user

    class Meta:
        table = 'users'

    class PydanticMeta:
        computed = ["full_name"]

