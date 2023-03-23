from rest_framework import serializers
from .models import Book, BooksList


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = BooksList
        fields = ['name', 'books', 'price', ]

    def get_price(self, book_list):
        result = 0
        for book in book_list.books.all():
            result += book.price

        return result
