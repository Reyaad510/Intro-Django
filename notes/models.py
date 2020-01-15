from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

# auto_now_add only sets on create
# auto_now sets on both create and update

# ./manage.py dbshell
# - .tables, pragma table_info(notes_note);
# - .headers on, .mode column, SELECT * FROM notes_note;
# control D out or .exit


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


# importing django built in user class model with a foreign key
# foreign key creates reference to data on another table. Works like pointer in C
# on_delete=models.CASCADE helps with integrity of the data
class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
