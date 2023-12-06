from colorama import init; init()

from app import drivers
from app.settings import parser



def start_app(driver):
	app = driver.create_app()
	driver.app_executor(app)


def main():
	args = parser.parse_args()
	driver = drivers.__getattribute__(args.driver)
	start_app(driver)


main()
