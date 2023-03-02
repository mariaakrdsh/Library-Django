from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from order.models import Order
from author.models import Author
from authentication.models import CustomUser
from .forms import AuthorForm, BookForm, OrderForm
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
def all_books(request):
    books = Book.objects.all()
    orders = Order.objects.all()
    user = request.user
    if user.is_staff:
        return render(request, 'staff_all_books.html', {'books': books, 'orders': orders})
    else:
        return render(request, 'all_books.html', {'books': books})


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    if user.is_staff:
        return render(request, 'staff_book_detail.html', {'book': book})
    else:
        return render(request, 'book_detail.html', {'book': book})


def book_form(request, book_id=0):
    user = request.user
    if request.method == "GET":
        if book_id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(instance=book)
        if user.is_staff:
            return render(request, 'book_form.html', {'form': form})
    else:
        if book_id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/all')


@login_required
def ordered_books(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    Order.objects.create(user=request.user, book=book)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders, 'message': 'Your order is accepted'})


@login_required
def find_book(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(name__icontains=query)
    else:
        books = []
    return render(request, 'search_book.html', {'books': books})


@login_required
def author_detail(request, author_id=0):
    user = request.user
    if request.method == "GET":
        if author_id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=author_id)
            form = AuthorForm(instance=author)
        if user.is_staff:
            return render(request, 'author_detail.html', {'form': form})
    else:
        if author_id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=author_id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('/authors')


@login_required
def list_of_authors(request):
    authors = Author.objects.all()
    user = request.user
    if user.is_staff:
        return render(request, 'list_of_authors.html', {'authors': authors})
    else:
        return redirect('/all')


@login_required
def user_detail(request, customer_id):
    customer = get_object_or_404(CustomUser, pk=customer_id)
    orders = Order.objects.filter(user=customer)
    user = request.user
    if user.is_staff:
        return render(request, 'user_detail.html', {'customer': customer, 'orders': orders})
    else:
        return redirect('/all')


@login_required
def list_of_orders(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('list_of_orders')
    else:
        orders = Order.objects.all()
        user = request.user
        if user.is_staff:
            order_form = OrderForm()
            context = {'orders': orders, 'order_form': order_form}
            return render(request, 'list_of_orders.html', context)
        else:
            return redirect('/all')


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('my_orders')
    else:
        form = OrderForm()
    return render(request, 'my_orders.html', {'orders': orders, 'form': form})
