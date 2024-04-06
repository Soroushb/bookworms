from django.contrib import admin

# Register your models here.
from .models import Book
from .models import BookClub
from .models import Discussion

admin.site.register(Book)
admin.site.register(BookClub)
admin.site.register(Discussion)