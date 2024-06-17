from typing import Annotated
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
import enum
from sqlalchemy import ForeignKey, text

from datetime import datetime

from base import Base


created_at = Annotated[
    datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow
    ),
]


class StatusResponse(enum.Enum):
    NO_RESPONSE = "Без отклика"
    CALL = "Звонок"
    TEST_TASK = "Тестовое задание"
    REFUSE = "Отказ"
    OFFER = "Предложение"


class StatusVacancy(enum.Enum):
    OPEN = "Открыта"
    CLOSED = "Закрыта"
    ARCHIVED = "В архиве"


class Vacancy(Base):

    __tablename__ = "vacancies"

    title: Mapped[str]
    status_vacancy: Mapped[StatusVacancy] = mapped_column(
        default=StatusVacancy.OPEN
    )
    company_name: Mapped[str]
    contact_user: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    status_response: Mapped[StatusResponse] = mapped_column(
        default=StatusResponse.NO_RESPONSE)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __repr__(self):
        return f"<Vacancy {self.title}>"
