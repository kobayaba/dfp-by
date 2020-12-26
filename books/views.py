from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
)

from .models import Book

class BookListView(LoginRequiredMixin, generic.ListView):
	model = Book
	template_name = 'books/book_list.html'
	login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
	model = Book
	template_name = 'books/book_detail.html'
	login_url = 'account_login'
	permission_required = 'books.special_status'