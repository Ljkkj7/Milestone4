from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal
from marketplace.models import Sneaker


class SneakerModelTests(TestCase):
    """Test suite for the Sneaker model"""

    def setUp(self):
        """Create test user for testing"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_sneaker_creation(self):
        """Test creating a Sneaker instance"""
        sneaker = Sneaker.objects.create(
            name='Air Max 90',
            brand='Nike',
            size=Decimal('10.5'),
            price=Decimal('120.00'),
            description='Classic Air Max',
            owner=self.user
        )
        self.assertEqual(sneaker.name, 'Air Max 90')
        self.assertEqual(sneaker.brand, 'Nike')
        self.assertEqual(sneaker.size, Decimal('10.5'))
        self.assertEqual(sneaker.price, Decimal('120.00'))
        self.assertEqual(sneaker.owner, self.user)


class SneakerViewTests(TestCase):
    """Test suite for marketplace views"""

    def setUp(self):
        """Set up test client"""
        self.client = Client()

    def test_marketplace_view_status_code(self):
        """Test that marketplace view returns 200"""
        response = self.client.get(reverse('marketplace'))
        self.assertEqual(response.status_code, 200)


class SneakerAdminTests(TestCase):
    """Test suite for Sneaker model in admin"""

    def setUp(self):
        """Create admin user and test data"""
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_admin_login(self):
        """Test admin user can log in"""
        login_success = self.client.login(
            username='admin',
            password='adminpass123'
        )
        self.assertTrue(login_success)
