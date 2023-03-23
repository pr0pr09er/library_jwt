from django.contrib import admin
from .models import Book, BooksList

admin.site.register(Book)
admin.site.register(BooksList)
