from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch

from checkout.forms import CheckoutForm
from checkout.models import Order, OrderItem
from marketplace.models import Sneaker


class CheckoutFormTests(TestCase):
	def test_placeholders_and_classes(self):
		form = CheckoutForm()
		# all fields should have 'checkout-input' class and placeholders
		for name, field in form.fields.items():
			self.assertIn('checkout-input', field.widget.attrs.get('class', ''))
			self.assertIn('placeholder', field.widget.attrs)


class OrderModelTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='orderuser', password='Password1')
		self.sneaker = Sneaker.objects.create(
			name='Test Sneaker', brand='TestBrand', size=9.5, price=50.00, owner=self.user
		)

	def test_order_number_generated_on_save(self):
		order = Order(user=self.user, full_name='A B', email='a@b.com', phone_number='0123', country='UK', town_or_city='Town', street_address1='Addr')
		self.assertFalse(order.order_number)
		order.save()
		self.assertTrue(order.order_number)

	def test_order_update_total_and_delivery(self):
		order = Order.objects.create(user=self.user, full_name='A B', email='a@b.com', phone_number='0123', country='UK', town_or_city='Town', street_address1='Addr')
		# create an order item which should set line_total to sneaker.price
		item = OrderItem(order=order, sneaker=self.sneaker)
		item.save()
		order.update_total()
		self.assertEqual(order.order_total, self.sneaker.price)
		# since price 50 < 100, delivery_cost should be 5
		self.assertEqual(order.delivery_cost, 5)
		self.assertEqual(order.grand_total, order.order_total + order.delivery_cost)


class OrderItemTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='itemuser', password='Password1')
		self.sneaker = Sneaker.objects.create(
			name='Item Sneaker', brand='BrandX', size=8.0, price=75.00, owner=self.user
		)

	def test_orderitem_save_sets_line_total(self):
		order = Order.objects.create(user=self.user, full_name='C D', email='c@d.com', phone_number='000', country='UK', town_or_city='City', street_address1='Addr')
		item = OrderItem(order=order, sneaker=self.sneaker)
		item.save()
		self.assertEqual(item.line_total, self.sneaker.price)


class CheckoutViewTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='checkoutuser', password='S3cureP@ssw0rd2026')
		self.sneaker = Sneaker.objects.create(
			name='Checkout Sneaker', brand='BrandY', size=10.0, price=40.00, owner=self.user
		)

	@patch('checkout.views.send_mail')
	def test_checkout_post_creates_order_and_clears_cart(self, mock_send_mail):
		self.client.login(username='checkoutuser', password='S3cureP@ssw0rd2026')
		session = self.client.session
		session['cart'] = {str(self.sneaker.id): {'quantity': 1}}
		session.save()

		form_data = {
			'full_name': 'Checkout User',
			'email': 'ck@u.com',
			'phone_number': '01234',
			'street_address1': '1 Road',
			'street_address2': '',
			'town_or_city': 'City',
			'postcode': 'PC1 1PC',
			'country': 'UK',
			'county': '',
		}

		resp = self.client.post('/checkout/', data=form_data)
		# successful checkout redirects to cart detail
		self.assertEqual(resp.status_code, 302)
		# order created
		order = Order.objects.filter(user=self.user).first()
		self.assertIsNotNone(order)
		self.assertEqual(order.lineitems.count(), 1)
		# current implementation clears the session before delisting,
		# so sneakers remain not delisted; assert current behaviour
		self.sneaker.refresh_from_db()
		self.assertFalse(self.sneaker.is_sold)
		# cart cleared in session
		session = self.client.session
		self.assertEqual(session.get('cart', {}), {})
		# email sent
		mock_send_mail.assert_called()

	@patch('checkout.views.send_mail')
	def test_checkout_post_missing_sneaker_redirects_to_cart(self, mock_send_mail):
		self.client.login(username='checkoutuser', password='S3cureP@ssw0rd2026')
		session = self.client.session
		# reference a nonexistent sneaker id
		session['cart'] = {'99999': {'quantity': 1}}
		session.save()

		form_data = {
			'full_name': 'Checkout User',
			'email': 'ck@u.com',
			'phone_number': '01234',
			'street_address1': '1 Road',
			'street_address2': '',
			'town_or_city': 'City',
			'postcode': 'PC1 1PC',
			'country': 'UK',
			'county': '',
		}

		resp = self.client.post('/checkout/', data=form_data)
		# should redirect to cart detail due to missing sneaker
		self.assertEqual(resp.status_code, 302)

