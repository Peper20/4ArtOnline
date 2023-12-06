from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


from app.settings import config


from .models import Base # noqa



engine = create_async_engine(config.db.url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
	async with async_session_maker() as session:
		yield session
