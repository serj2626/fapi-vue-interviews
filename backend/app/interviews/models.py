from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String
import enum
from sqlalchemy import ForeignKey
from app.config.base import Base
from datetime import datetime


class StatusResponse(enum.Enum):
    NO_RESPONSE = "Без отклика"
    CALL = "Звонок"
    TEST_TASK = "Тестовое задание"
    REFUSE = "Отказ"
    OFFER = "Предложение"


class StatusVacancy(enum.Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"


class Vacancy(Base):

    __tablename__ = "vacancies"

    title: Mapped[str]
    status_vacancy: Mapped[StatusVacancy] = mapped_column(
        default=StatusVacancy.OPEN)
    company_name: Mapped[str]
    contact_user: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    status_response: Mapped[StatusResponse] = mapped_column(
        default=StatusResponse.NO_RESPONSE)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"<Vacancy {self.title}>"
