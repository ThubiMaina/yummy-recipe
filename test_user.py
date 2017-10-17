"""test methods for the user class"""
import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Perform unit testing for the User class
    """
    def setUp(self):
        """The setUp method before doing the tests"""
        self.newUser = User()

    def test_create_account(self):
        """ method to test for creating user account"""
        self.newUser.users = {}
        current_count = len(self.newUser.users)
        result = self.newUser.register('email@mail.com', 'name', '1234', '1234')
        self.assertEqual(current_count+1, result, "User succesfully created")

if __name__ == 'main':
    unittest.main()
