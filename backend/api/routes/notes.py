from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist
from typing import List

from ...db_config.models import Note, NoteCreate, User, NoteResponse, UsernameInput, DeleteNoteRequest

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

@notes_router.post("/get_all_notes/")
async def get_all_notes(input_data: UsernameInput) -> List[NoteResponse]:
    try:
        # Находим пользователя по username
        user = await User.get(username=input_data.username)

        # Получаем все заметки пользователя
        notes = await user.notes.all()

        # Преобразуем заметки в формат JSON
        return [
            NoteResponse(
                id=note.id,
                title=note.title,
                content=note.content,
                created_at=str(note.created_at),
                updated_at=str(note.updated_at),
            )
            for note in notes
        ]

    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

@notes_router.post("/delete_note/")
async def delete_note(request_data: DeleteNoteRequest):
    try:
        # Проверяем, существует ли заметка с указанным ID
        note = await Note.get_or_none(id=request_data.note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Заметка не найдена")

        # Удаляем заметку
        await note.delete()
        return {"message": "Заметка успешно удалена"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при удалении заметки: {str(e)}")