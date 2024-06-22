from .crud import VacancyCRUD
from app.users import User
from .schemas import SVacancyCreate
from fastapi import Depends
from app.users.dependencies import get_current_user


async def create_interview(
        user: User = Depends(get_current_user),
        data: SVacancyCreate = Depends()):
    
    await VacancyCRUD.add_obj(
        user_id=user.id,
        **data.model_dump()
    )
  
    return {"user": user, "data": data}
