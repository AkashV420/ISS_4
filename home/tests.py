from django.test import TestCase

# Create your tests here.

class HomeTests(TestCase):

    def test_basic(self):
        response = self.client.get('/')
        self.assertNotContains(
                response, 'Invalid HTML'
                )

