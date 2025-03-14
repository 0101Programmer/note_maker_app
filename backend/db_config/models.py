from pydantic import BaseModel
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    notes = fields.ReverseRelation["Note"]

class Note(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    user = fields.ForeignKeyField("models.User", related_name="notes")

# Модель данных для создания заметки
class NoteCreate(BaseModel):
    title: str
    content: str