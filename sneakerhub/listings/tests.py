from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import ListingCreationForm
from marketplace.models import Sneaker


class ListingCreationFormTests(TestCase):
    """Test the ListingCreationForm ModelForm."""

    def test_form_valid_with_all_fields(self):
        """Test form is valid when all required fields are provided."""
        form_data = {
            'name': 'Air Jordan 1',
            'brand': 'Nike',
            'size': '10.5',
            'price': '150.00',
            'description': 'A classic sneaker in great condition with original box.',
        }
        form = ListingCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_without_name(self):
        """Test form is invalid when name is missing."""
        form_data = {
            'brand': 'Nike',
            'size': '10.5',
            'price': '150.00',
            'description': 'A classic sneaker in great condition.',
        }
        form = ListingCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_form_invalid_without_required_fields(self):
        """Test form is invalid when required fields are missing."""
        form_data = {'name': 'Air Jordan 1'}
        form = ListingCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('brand', form.errors)
        self.assertIn('size', form.errors)
        self.assertIn('price', form.errors)

    def test_form_description_validation_too_short(self):
        """Test form rejects description shorter than 10 characters."""
        form_data = {
            'name': 'Air Jordan 1',
            'brand': 'Nike',
            'size': '10.5',
            'price': '150.00',
            'description': 'short',  # Only 5 characters
        }
        form = ListingCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)
        self.assertIn('at least 10 characters', str(form.errors['description']))

    def test_form_description_validation_exact_length(self):
        """Test form accepts description exactly 10 characters."""
        form_data = {
            'name': 'Air Jordan 1',
            'brand': 'Nike',
            'size': '10.5',
            'price': '150.00',
            'description': '1234567890',  # Exactly 10 characters
        }
        form = ListingCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_accepts_optional_image(self):
        """Test form is valid without an image file."""
        form_data = {
            'name': 'Air Jordan 1',
            'brand': 'Nike',
            'size': '10.5',
            'price': '150.00',
            'description': 'A classic sneaker in great condition.',
        }
        form = ListingCreationForm(data=form_data)
        self.assertTrue(form.is_valid())


class createListingViewTests(TestCase):
    """Test suite for createListingView."""

    def setUp(self):
        """Set up test client and user."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.create_listing_url = reverse('create_listing')

    def test_create_listing_view_requires_login(self):
        """Test that unauthenticated users are redirected to login."""
        response = self.client.get(self.create_listing_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_create_listing_view_get_authenticated(self):
        """Test GET request shows the form for authenticated users."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.create_listing_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ListingCreationForm)

    def test_create_listing_view_post_valid_creates_sneaker(self):
        """Test valid POST creates a new Sneaker with owner set."""
        self.client.login(username='testuser', password='testpass123')
        form_data = {
            'name': 'Air Jordan 1',
            'brand': 'Nike',
            'size': '10.5',
            'price': '150.00',
            'description': 'A classic sneaker in great condition.',
        }
        response = self.client.post(self.create_listing_url, data=form_data)

        self.assertTrue(Sneaker.objects.filter(name='Air Jordan 1').exists())
        sneaker = Sneaker.objects.get(name='Air Jordan 1')
        
        self.assertEqual(sneaker.owner, self.user)
        self.assertEqual(sneaker.brand, 'Nike')
        self.assertEqual(str(sneaker.size), '10.5')
        self.assertEqual(str(sneaker.price), '150.00')