from sqlalchemy import and_, insert, select, update

from app.core import async_session
from app.service import BaseCRUD

from .models import Vacancy


class VacancyCRUD(BaseCRUD):
    model = Vacancy
