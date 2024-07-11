# test_views.py
import unittest
from myapp import app

class TestViews(unittest.TestCase):
    def setUp(self):
        # Setup test client
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
