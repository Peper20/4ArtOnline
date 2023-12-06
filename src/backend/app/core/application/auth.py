from uuid import UUID


from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy


from app.settings import SECRET
from app.drivens.database.models.auth import User


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
	reset_password_token_secret = SECRET
	verification_token_secret = SECRET


def get_jwt_strategy() -> JWTStrategy:
	return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


cookie_transport = CookieTransport(cookie_max_age=3600)
auth_backend = AuthenticationBackend(
	name='jwt',
	transport=cookie_transport,
	get_strategy=get_jwt_strategy,
)


