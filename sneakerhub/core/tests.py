from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from unittest.mock import patch

from core import views


class CustomerFormTests(TestCase):
	def test_clean_email_duplicate(self):
		User.objects.create_user(username='existing', email='dup@example.com', password='Password1')
		data = {
			'username': 'newuser',
			'email': 'dup@example.com',
			'password1': 'S3cureP@ssw0rd2026',
			'password2': 'S3cureP@ssw0rd2026',
		}
		form = views.CustomerUserCreationForm(data)
		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors)

	@patch('core.views.send_mail')
	def test_signup_creates_user_and_sends_email(self, mock_send_mail):
		client = Client()
		resp = client.post(reverse('signup'), {
			'username': 'tester',
			'email': 'tester@example.com',
			'password1': 'S3cureP@ssw0rd2026',
			'password2': 'S3cureP@ssw0rd2026',
		})
		self.assertEqual(resp.status_code, 302, msg=resp.content.decode())
		self.assertTrue(User.objects.filter(username='tester').exists())
		mock_send_mail.assert_called()


class AuthViewsTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='loginuser', email='login@example.com', password='Password1')

	def test_login_success_redirects(self):
		resp = self.client.post(reverse('login'), {'username': 'loginuser', 'password': 'Password1'})
		self.assertEqual(resp.status_code, 302)
		self.assertIn(reverse('marketplace'), resp['Location'])

	def test_login_invalid_shows_error(self):
		resp = self.client.post(reverse('login'), {'username': 'loginuser', 'password': 'wrong'})
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, "Invalid username or password.")

	def test_logout_redirects_home(self):
		self.client.login(username='loginuser', password='Password1')
		resp = self.client.get(reverse('logout'))
		self.assertEqual(resp.status_code, 302)
		self.assertIn(reverse('home'), resp['Location'])
		

class EmailFunctionTests(TestCase):
	@patch('core.views.send_mail')
	def test_send_signup_confirmation_email(self, mock_send):
		user = User.objects.create_user(username='mailuser', email='m@example.com', password='Password1')
		views.sendSignUpConfirmationEmail(user)
		mock_send.assert_called_once()
		# send_mail positional args: subject, plain_message, from_email, recipient_list, ...
		called_args = mock_send.call_args[0]
		self.assertEqual(called_args[3], [user.email])


class AuthCheckTests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='u', email='u@example.com', password='Password1')

	def test_authcheck_anonymous(self):
		req = self.factory.get('/')
		req.user = AnonymousUser()
		self.assertFalse(views.authCheck(req))

	def test_authcheck_authenticated(self):
		req = self.factory.get('/')
		req.user = self.user
		self.assertTrue(views.authCheck(req))

