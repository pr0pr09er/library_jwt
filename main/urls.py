from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_books/', views.get_books, name='get_books'),
    path('get_books/<int:pk>/', views.get_book, name='get_book'),
    path('create_book/', views.create_book, name='create_book'),
    path('update_book/', views.update_book, name='update_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('get_book_lists/', views.get_books_list, name='get_book_lists'),
    path('get_book_lists/<int:pk>/', views.get_book_list, name='get_book_list'),
    path('create_book_list/', views.create_book_list, name='create_book_list'),
    path('update_book_list/<int:pk>/', views.update_book_list, name='update_book_list'),
    path('delete_book_list/<int:pk>/', views.delete_book_list, name='delete_book_list'),
]
