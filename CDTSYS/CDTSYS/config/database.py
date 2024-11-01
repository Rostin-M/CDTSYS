from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from CDTSYS.config import config

engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()