import enum
from .models import Vacancy
from pydantic import BaseModel
from pydantic import EmailStr


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


class SVacancyCreate(BaseModel):
    title: str
    status_vacancy: StatusVacancy
    company_name: str
    contact_user: str | None = None
    status_response: StatusResponse

    class Config:
        orm_mode = True
