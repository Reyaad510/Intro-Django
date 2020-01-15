from django.contrib import admin
from .models import Note


# we do this because auto_now is read only
# Doing this will allow created_at and last_modified to show in the admin interface
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


# Register your models here.
# to add more just do admin.site.register(insertname)
admin.site.register(Note, NoteAdmin)
