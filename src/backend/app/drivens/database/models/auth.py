from fastapi_users.db import SQLAlchemyBaseUserTableUUID


from .base import Base




class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user'


    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

