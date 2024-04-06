from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class BookClub(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    books = models.ManyToManyField(Book, related_name='book_clubs')
    members = models.ManyToManyField(User, related_name='member_of')

    def __str__(self):
        return self.name

class Discussion(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    club = models.ForeignKey(BookClub, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    started_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic