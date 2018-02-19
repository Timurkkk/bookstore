from django.shortcuts import render_to_response

from .models import Book

def latest_books (request):
    book_list=Book.objects.order_by ('-pub_date')[:10]
    return render_to_response ('index.html', {'book_list':book_list})
