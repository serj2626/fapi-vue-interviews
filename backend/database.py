from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import settings



engine = create_async_engine(url=settings.DB_URL)
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)

from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()+'s'
print(settings)