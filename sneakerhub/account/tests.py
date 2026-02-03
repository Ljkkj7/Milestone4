from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError

from marketplace.models import Sneaker
from account.models import WishlistItem, CreatorAccountModel


class CreatorAccountModelTests(TestCase):
    def test_str(self):
        user = User.objects.create_user(username='creator', password='Password1')
        cam = CreatorAccountModel.objects.create(user=user, bio='bio')
        self.assertIn('creator', str(cam))


class WishlistViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='wishuser', password='S3cureP@ssw0rd2026')
        self.other = User.objects.create_user(username='other', password='Password1')
        self.sneaker = Sneaker.objects.create(name='Wish Sneak', brand='B', size=9.0, price=30.0, owner=self.other)

    def test_add_to_wishlist_creates_item_and_prevents_duplicates(self):
        self.client.login(username='wishuser', password='S3cureP@ssw0rd2026')
        resp = self.client.get(reverse('wishlist_add', kwargs={'sneaker_id': self.sneaker.id}))
        # view redirects to sneaker detail on success
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(WishlistItem.objects.filter(user=self.user, sneaker=self.sneaker).exists())

        # adding again should redirect with error param and not create duplicate
        resp2 = self.client.get(reverse('wishlist_add', kwargs={'sneaker_id': self.sneaker.id}))
        self.assertEqual(resp2.status_code, 302)
        # ensure only one exists
        self.assertEqual(WishlistItem.objects.filter(user=self.user, sneaker=self.sneaker).count(), 1)

    def test_remove_from_wishlist_deletes_item_or_errors(self):
        self.client.login(username='wishuser', password='S3cureP@ssw0rd2026')
        # removing when not present should redirect with ?error=not_in_wishlist
        resp = self.client.get(reverse('wishlist_remove', kwargs={'sneaker_id': self.sneaker.id}))
        self.assertEqual(resp.status_code, 302)

        # add then remove
        WishlistItem.objects.create(user=self.user, sneaker=self.sneaker)
        resp2 = self.client.get(reverse('wishlist_remove', kwargs={'sneaker_id': self.sneaker.id}))
        self.assertEqual(resp2.status_code, 302)
        self.assertFalse(WishlistItem.objects.filter(user=self.user, sneaker=self.sneaker).exists())


class AccountPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='accuser', password='S3cureP@ssw0rd2026')
        self.other = User.objects.create_user(username='accother', password='Password1')

    def test_account_page_permission_denied_for_other_user(self):
        self.client.login(username='accuser', password='S3cureP@ssw0rd2026')
        resp = self.client.get(reverse('account', kwargs={'user_id': self.other.id}))
        self.assertEqual(resp.status_code, 302)
        # redirected to permission denied
        self.assertIn(reverse('errorhandler:permission_denied'), resp['Location'])

    def test_account_page_renders_for_owner(self):
        self.client.login(username='accuser', password='S3cureP@ssw0rd2026')
        resp = self.client.get(reverse('account', kwargs={'user_id': self.user.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('available_sneakers', resp.context)
from django.test import TestCase

# Create your tests here.
