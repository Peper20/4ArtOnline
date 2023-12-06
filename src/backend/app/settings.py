from dataclasses import dataclass
from os import environ




# crypto area {

SECRET = 'S3V5LU11c3QtQmUtYXQtbGVhc3QtdzItYnl0ZXMtaW4tbGVuZ3RoIq'

# }


# db area {

@dataclass
class DbConfig:
	user: str
	password: str
	host: str
	name: str

	@property
	def url(self):
		return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}'

# }


# main config area {

from dotenv import load_dotenv

@dataclass
class Config:
	db: DbConfig


def load_config():
	load_dotenv()

	return Config(
		db=DbConfig(
			environ.get('user'),
			environ.get('password'),
			environ.get('host'),
			environ.get('name'),
		),
	)

config = load_config()

# }


# argparser area {

from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--driver', required=True, choices=['api'])

# }