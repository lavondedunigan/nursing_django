from django.contrib import admin
from .models import Note,  NoteComment

# Register your models here.
admin.site.register(Note)
admin.site.register(NoteComment)
# admin.site.register(NoteComment)  # This line is already included in the import above



