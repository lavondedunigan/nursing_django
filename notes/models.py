from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(User, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
    
class NoteComment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
    