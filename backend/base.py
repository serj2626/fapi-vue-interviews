from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declared_attr


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()+'s'
