import os

from environs import Env

env = Env()

env.read_env(os.path.realpath(".env"))
