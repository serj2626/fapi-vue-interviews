from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import Integer, String

from service.base import Base


class User(Base):

    username: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False, server_default="false")
    is_verified: Mapped[bool] = mapped_column(default=False, server_default="false")

    def __repr__(self):
        return f"<User {self.username}>"
