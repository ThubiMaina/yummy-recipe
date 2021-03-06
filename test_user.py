"""test methods for the user class"""
import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Perform unit testing for the User class
    """
    # pylint: disable-msg=C0103
    def setUp(self):
        """The setUp method before doing the tests"""
        self.newUser = User()
        self.newUser.users = {}

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

    def test_null_password(self):
        """ defining method to check for null pasword"""
        result = self.newUser.register('erick@gmail.com', 'Erick', '', '1234')
        self.assertEqual(6, result, 'enter the password')

    def test_special_characters(self):
        """defining method to test for special characters in the user name"""
        result = self.newUser.register('erick@gmail.com', '##', '1234', '1234')
        self.assertEqual(5, result, "Username cannot have special characters")

    def test_wrong_login_password(self):
        """defining method to test if login password is equal to register passsword"""
        self.newUser.register('erick@mail.com', 'Erick', 'pass', 'pass')
        result = self.newUser.login('erick@mail.com', 'pass123')
        self.assertEqual(2, result, "password mismatch")

    def test_email_exists(self):
        """method to check if email provided has been used to register another user"""
        self.newUser.register('erick@gmail.com', 'Erick', '1234', '1234')
        result = self.newUser.register('erick@gmail.com', 'Maina', 'pass', 'pass')
        self.assertEqual(4, result, 'This email has been registered')

    def test_wrong_login_email(self):
        """defining method to test if login email is equal to register email"""
        self.newUser.register('erick@gmail.com', 'Erick', '1234', '1234')
        result = self.newUser.login('erick35@gmail.com', 'pass')
        self.assertEqual(3, result, "wrong password")

    def test_login_null_email(self):
        """defining method to test for null login email"""
        result = self.newUser.login('', '1234')
        self.assertEqual(4, result, "Please fill the email field")

    def test_login_null_password(self):
        """defining method to test for null login password"""
        result = self.newUser.login('erick@gmail.com', '')
        self.assertEqual(4, result, "Please fill the password field")

if __name__ == 'main':
    unittest.main()
