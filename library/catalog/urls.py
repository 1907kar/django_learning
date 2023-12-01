from django.urls import path
from . import views

# Added this to use it in redirect - Do not use this when you are going to use reverse from models
# Its causing errors which is not clear
# app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    # the name should be as defined in the models get_absolute_url
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('restricted_view/', views.restricted_view, name='restricted_view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.UserCheckedOutBooks.as_view(), name='profile'),
]