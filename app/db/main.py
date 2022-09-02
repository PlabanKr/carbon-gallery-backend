from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# we are using psycopg2-binary as our database driver
DATABASE_URL = "postgresql://postgres:password@localhost/carbon_gallery"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)