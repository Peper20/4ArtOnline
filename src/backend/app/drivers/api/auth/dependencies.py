from uuid import UUID


from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Depends


from app.core.application.auth import auth_backend, UserManager

from app.drivens.database.db import AsyncSession, get_async_session
from app.drivens.database.models import User




async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
	yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)

