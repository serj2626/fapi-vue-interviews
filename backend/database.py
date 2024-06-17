from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_async_engine(url=settings.DB_URL, echo=settings.DB_ECHO)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
