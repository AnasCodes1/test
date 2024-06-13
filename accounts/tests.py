from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="testuser@gmail.com", password="testing321"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser(
            username="superadmin", email="superadmin@gmail.com", password="testing321"
        )
        self.assertEqual(admin.username, "superadmin")
        self.assertEqual(admin.email, "superadmin@gmail.com")
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

