from sqlalchemy import create_engine


from src.config.config import DATABASE_URL

engine = create_engine(DATABASE_URL)


