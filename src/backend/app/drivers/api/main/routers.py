from fastapi import FastAPI


from app.drivers.api.root import router as root_router
from app.drivers.api.auth import router as auth_router




def init_routers(app: FastAPI) -> None:
	app.include_router(root_router)
	app.include_router(auth_router)
