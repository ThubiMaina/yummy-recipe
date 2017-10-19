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
        self.username = 'Erick'
        self.email = 'erick@gmail.com'
        self.password = '1234'
        self.cpassword = '1234'

    def test_create_user(self):
        """ method to test for success in creating user account"""
        new_user = self.newUser.register(self.email, self.username, self.password, self.cpassword)
        self.assertEqual(1, new_user, "Successfully created")

    def test_null_username(self):
        """method to checking when user name is empty"""
        result = self.newUser.register(self.email, '', self.password, self.cpassword)
        self.assertEqual("blank fields", result)

    def test_null_email(self):
        """method to check if the email is empty"""
        result = self.newUser.register('', self.username, self.password, self.cpassword)
        self.assertEqual("blank fields", result, 'Email cannot be empty')

    def test_cpassword_is_password(self):
        """defining method to test for created user's password is equal to confirm password"""
        output = self.newUser.register(self.email, self.username, self.password, 'pass')
        self.assertEqual("password mismatch", output, "password mismatch")

    def test_null_password(self):
        """ defining method to check for null pasword"""
        result = self.newUser.register(self.email, self.username, '', self.cpassword)
        self.assertEqual("blank fields", result, 'enter the password')

   
    def test_special_characters(self):
        """defining method to test for special characters in the user name"""
        result = self.newUser.register(self.email, "##", self.password, self.cpassword)
        self.assertEqual("special characters in username", result, 'user name cannot have special characters')

    def test_wrong_login_password(self):
        """defining method to test if login password is equal to register passsword"""
        self.newUser.register(self.email, self.username, self.password, self.cpassword)
        result = self.newUser.login('erick@mail.com', 'pass123')
        self.assertEqual(3, result,)

    def test_email_exists(self):
        """method to check if email provided has been used to register another user"""
        self.newUser.register(self.email, self.username, self.password, self.cpassword)
        result = self.newUser.register('erick@gmail.com', 'Maina', 'pass', 'pass')
        self.assertEqual("email registered", result, 'This email has been registered')

    def test_wrong_login_email(self):
        """defining method to test if login email is equal to register email"""
        self.newUser.register(self.email, self.username, self.password, self.cpassword)
        result = self.newUser.login('erick35@gmail.com', '1234')
        self.assertEqual(3, result, "wrong password")

    def test_login_null_email(self):
        """defining method to test for null login email"""
        result = self.newUser.login('', self.cpassword)
        self.assertEqual(4, result, "Please fill the email field")

    def test_login_null_password(self):
        """defining method to test for null login password"""
        result = self.newUser.login(self.email, '')
        self.assertEqual(4, result, "Please fill the password field")

if __name__ == 'main':
    unittest.main()
