"""test methods for the user class"""
import unittest
import user
from user import User
from app import app

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
        self.password = '123456'
        self.cpassword = '123456'
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        """ method to test for success in creating user account"""
        new_user = self.newUser.register(self.email, self.username, self.password, self.cpassword)
        self.assertEqual(1, new_user)

    def test_success_login(self):
        """ method to test for login success"""
        result = self.newUser.login(self.email, self.password)
        self.assertEqual(1, result)

    def test_application_up_and_running(self):
        """ Testing the index link"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_login_url(self):
        """ Testing the user login link"""
        result = self.app.get('/login/')
        self.assertEqual(result.status_code, 404)

    def test_register_url(self):
        """ Testing the user register link"""
        result = self.app.get('/register')
        self.assertEqual(result.status_code, 200)

    def test_create_url(self):
        """ Testing the user create category link"""
        result = self.app.get('/create/')
        self.assertEqual(result.status_code, 200)

    def test_null_username(self):
        """method to checking when user name is empty"""
        result = self.newUser.register(self.email, '', self.password, self.cpassword)
        self.assertEqual('You have blank fields', result)

    def test_null_email(self):
        """method to check if the email is empty"""
        result = self.newUser.register('', self.username, self.password, self.cpassword)
        self.assertEqual('You have blank fields', result, 'Email cannot be empty')

    def test_cpassword_is_password(self):
        """defining method to test for created user's password is equal to confirm password"""
        output = self.newUser.register(self.email, self.username, self.password, 'pass')
        self.assertEqual("password mismatch", output, "password mismatch")

    def test_null_password(self):
        """ defining method to check for null pasword"""
        result = self.newUser.register(self.email, self.username, '', self.cpassword)
        self.assertEqual('You have blank fields', result, 'enter the password')

    def test_special_characters(self):
        """defining method to test for special characters in the user name"""
        result = self.newUser.register(self.email, "##", self.password, self.cpassword)
        self.assertEqual("special characters in username", result, 'No characters')

    def test_email_exists(self):
        """method to check if email provided has been used to register another user"""
        self.newUser.register(self.email, self.username, self.password, self.cpassword)
        result = self.newUser.register('erick@gmail.com', 'Maina', 'pass', 'pass')
        self.assertEqual("email registered", result)

    def test_wrong_login_email(self):
        """defining method to test if login email is equal to register email"""
        self.newUser.register(self.email, self.username, self.password, self.cpassword)
        result = self.newUser.login('erick35@gmail.com', '1234')
        self.assertEqual("not registered", result, "Email does not exist")

    def test_login_null_email(self):
        """defining method to test for null login email"""
        result = self.newUser.login('', self.cpassword)
        self.assertEqual("blank fields", result, "Please fill the email field")

    def test_login_null_password(self):
        """defining method to test for null login password"""
        result = self.newUser.login(self.email, '')
        self.assertEqual("blank fields", result, "Please fill the password field")


if __name__ == 'main':
    unittest.main()
