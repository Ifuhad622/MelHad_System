# test_models.py
import unittest
from myapp.models import User, db

class TestModels(unittest.TestCase):
    def setUp(self):
        # Setup test environment, e.g., initialize database
        self.user = User(username='testuser', email='test@example.com')
        db.session.add(self.user)
        db.session.commit()

    def test_user_creation(self):
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
