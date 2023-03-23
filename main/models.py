from django.db import models
from isbn_field.fields import ISBNField


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    ISBN = ISBNField(null=True, blank=True)
    price = models.IntegerField()


class BooksList(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField("Book")
