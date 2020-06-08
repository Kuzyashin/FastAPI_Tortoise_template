from tortoise import Model
from tortoise import fields


class BaseDBModel(Model):
    id = fields.BigIntField(pk=True, index=True)

    class Meta:
        abstract = True


class BaseCreatedAtModel:
    created_at = fields.DatetimeField(auto_now_add=True)


class BaseCreatedUpdatedAtModel:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
