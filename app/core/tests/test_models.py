from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

	def test_create_user_with_email_successful(self):
		""" test create new user with an email is successful"""
		email 	= "ahmed.mansy@segmatek.com"
		password= "Agmansy0100"
		user 	= get_user_model().objects.create_user(
			email = email,
			password = password
		)
		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalized(self):
		""" test that email for new user is normalized"""
		email 	= "ahmed.mansy@SEGMATEK.com"
		password= "Agmansy0100"
		user 	= get_user_model().objects.create_user(email, password)
		
		self.assertEqual(user.email, email.lower())
		self.assertTrue(user.check_password(password))


	def test_new_user_invalid_email(self):
		""" test creating new user with no email address"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'test123')



	def test_create_new_superuser(self):
		""" test that email for new user is normalized"""
		email 	= "ahmed.mansy@SEGMATEK.com"
		password= "Agmansy0100"
		user 	= get_user_model().objects.create_superuser(email, password)
		
		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)