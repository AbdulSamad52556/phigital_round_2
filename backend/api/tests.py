from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Role, Groups, UserRole, UserGroup

CustomUser = get_user_model()

class AccessControlTests(APITestCase):
    def setUp(self):
        admin_role = Role.objects.create(name="Admin")
        manager_role = Role.objects.create(name="Manager")
        premium_group = Groups.objects.create(name="Premium")
        non_premium_group = Groups.objects.create(name="Non-Premium")

        self.admin_user = CustomUser.objects.create_user(username="admin", email="admin@test.com", password="password", user_type="normal")
        UserRole.objects.create(user=self.admin_user, role=admin_role)
        UserGroup.objects.create(user=self.admin_user, group=premium_group)

        self.manager_user = CustomUser.objects.create_user(username="manager", email="manager@test.com", password="password", user_type="normal")
        UserRole.objects.create(user=self.manager_user, role=manager_role)
        UserGroup.objects.create(user=self.manager_user, group=non_premium_group)

        self.manager_user2 = CustomUser.objects.create_user(username="manager2", email="manager2@test.com", password="password", user_type="normal")
        UserRole.objects.create(user=self.manager_user2, role=manager_role)
        UserGroup.objects.create(user=self.manager_user2, group=premium_group)

        self.manager_user3 = CustomUser.objects.create_user(username="manager3", email="manager3@test.com", password="password", user_type="corporate")
        UserRole.objects.create(user=self.manager_user3, role=manager_role)
        UserGroup.objects.create(user=self.manager_user3, group=non_premium_group)

    def test_admin_access(self):
        self.client.login(username="admin", password="password")
        response = self.client.get("/assistantflightbooking")
        self.assertEqual(response.status_code, 200)

    def test_manager_access(self):
        self.client.login(username="manager", password="password")
        response = self.client.get("/assistanthotelbooking")
        self.assertEqual(response.status_code, 403)

    def test_premium_user_access(self):
        self.client.login(username="manager2", password="password")
        response = self.client.get("/assistantflightbooking")
        self.assertEqual(response.status_code, 200)

    def test_non_premium_user_access(self):
        self.client.login(username="manager3", password="password")
        response = self.client.get("/assistantflightbooking")
        self.assertEqual(response.status_code, 200)