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

    def test_null_username(self):
        """method to checking when user name is empty"""
        result = self.newUser.register('erick@gmail.com', '', '1234', '1234')
        self.assertEqual(6, result, 'User name cannot be empty')

    def test_null_email(self):
        """method to check if the email is empty"""
        result = self.newUser.register('', 'Erick', '1234', '1234')
        self.assertEqual(6, result, 'Email cannot be empty')

    def test_cpassword_is_password(self):
        """defining method to test for created user's password is equal to confirm password"""
        output = self.newUser.register('erick@email.com', 'Erick', '1234', '124')
        self.assertEqual(3, output, "password mismatch")

if __name__ == 'main':
    unittest.main()
