from django.contrib import admin
from django.urls import path
from authentication.views import login_view, register
from book.views import all_books, book_detail, ordered_books, my_orders, find_book, author_detail, \
    list_of_authors, user_detail, list_of_orders, book_form
from django.contrib.auth.views import LogoutView
from order.views import OrderList, OrderDetail
from book.views import BookList, BookDetail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', list_of_authors, name = 'list_of_authors'),
    path('all/', all_books, name = 'all_books'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book_form/<int:book_id>/', book_form, name='book_form'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('book/<int:book_id>/order/', ordered_books, name='ordered_books'),
    path('my_orders/', my_orders, name='my_orders'),
    path('find_book/', find_book, name='find_book'),
    path('login/', login_view, name='login'),
    path('orders/', list_of_orders, name = 'list_of_orders'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('user/<int:customer_id>/', user_detail, name='user_detail'),
    path('', register),
    path('api/v1/order/', OrderList.as_view(), name='order_list'),
    path('api/v1/order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('api/v1/books/', BookList.as_view()),
    path('api/v1/books/<int:pk>/', BookDetail.as_view()),

]