from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
	
	def test_create_user(self):
		user = get_user_model().objects.create_user(
			username='testuser',
			email='testuser@email.com',
			password='testpass123'
		)
		self.assertEqual(user.username, 'testuser')
		self.assertEqual(user.email, 'testuser@email.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_create_superuser(self):
		admin_user = get_user_model().objects.create_superuser(
			username='superadmin',
			email='superadmin@email.com',
			password='superadminpass123'
		)
		self.assertEqual(admin_user.username, 'superadmin')
		self.assertEqual(admin_user.email, 'superadmin@email.com')
		self.assertTrue(admin_user.is_active)
		self.assertTrue(admin_user.is_staff)
		self.assertTrue(admin_user.is_superuser)