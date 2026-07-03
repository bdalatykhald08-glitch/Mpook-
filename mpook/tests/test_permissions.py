from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIRequestFactory

class PermissionsQuickTest(TestCase):
    def test_is_authenticated_permission(self):
        
        permission = IsAuthenticated()
        
        class AnonymousUser: is_authenticated = False

        class AnonymousRequest: user = AnonymousUser()
               
        self.assertFalse(permission.has_permission(AnonymousRequest(), None))
        
        
        class AuthenticatedUser: is_authenticated = True

        class AuthenticatedRequest: user = AuthenticatedUser()
        
        self.assertTrue(permission.has_permission(AuthenticatedRequest(), None))




