from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # This links the book to the user who added it:
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title
