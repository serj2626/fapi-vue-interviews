from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import settings


engine = create_async_engine(url=settings.DB_URL)
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)
