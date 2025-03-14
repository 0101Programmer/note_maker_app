from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from ...db_config.models import Note, NoteCreate, User

notes_router = APIRouter(prefix="/notes", tags=["Notes"])

@notes_router.post("/create_note/{tg_username}")
async def create_note(tg_username: str, note_data: NoteCreate):
    try:
        # Находим пользователя по tg_username
        user = await User.get(username=tg_username)

        # Создаем заметку, связанную с пользователем
        await Note.create(
            title=note_data.title,
            content=note_data.content,
            user=user  # Связываем заметку с пользователем
        )
        return {"status": True, "message": "Note created"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create note: {str(e)}")