from .main import create_app


def app_executor(app):
	from uvicorn import run
	run(app, host='0.0.0.0')

