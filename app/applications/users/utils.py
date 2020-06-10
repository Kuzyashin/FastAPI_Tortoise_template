from datetime import datetime

from app.applications.users.models import User


async def update_last_login(user_id: int) -> None:
    user = await User.get(id=user_id)
    user.last_login = datetime.now()
    await user.save()
