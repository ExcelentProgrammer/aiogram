import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.env import env

db_url = f"{env.str('DB_ENGINE')}://{env.str('DB_USER')}:{env.str('DB_PASSWORD')}@{env.str('DB_HOST', 'localhost')}/{env.str('DB_NAME')}"

Base = sqlalchemy.orm.declarative_base()
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
