from django.test import TestCase
from .forms import ListingCreationForm


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
