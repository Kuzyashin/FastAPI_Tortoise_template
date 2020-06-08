from tortoise import models
from tortoise import fields


class BaseDBModel(models.Model):
    id = fields.BigIntField(pk=True, index=True)

    async def to_dict(self):
        d = {}
        for field in self._meta.db_fields:
            d[field] = getattr(self, field)
        for field in self._meta.backward_fk_fields:
            d[field] = await getattr(self, field).all().values()
        return d

    class Meta:
        abstract = True


class UUIDDBModel:
    hashed_id = fields.UUIDField(unique=True, pk=False)


class BaseCreatedAtModel:
    created_at = fields.DatetimeField(auto_now_add=True)


class BaseCreatedUpdatedAtModel:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
