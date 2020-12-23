from django.test import TestCase, Client
from django.urls import reverse


from .models import Book

class BookTests(TestCase):

	def setUp(self):
		self.book = Book.objects.create(
			title='Utopie ou la mort',
			author='Rene Dumont',
			price='24.00'
		)

	def test_book_listing(self):
		self.assertEqual(f'{self.book.title}', 'Utopie ou la mort')
		self.assertEqual(f'{self.book.author}', 'Rene Dumont')
		self.assertEqual(f'{self.book.price}', '24.00')


	def test_book_list_view(self):
		response = self.client.get(reverse('book_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Utopie ou la mort')
		self.assertTemplateUsed(response, 'books/book_list.html')


	def test_book_detail_view(self):
		response = self.client.get(self.book.get_absolute_url())
		no_response = self.client.get('/books/12345/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'Utopie ou la mort')
		self.assertTemplateUsed(response, 'books/book_detail.html')