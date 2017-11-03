""" The user class functions"""
import re
# pylint: disable=R0201
# pylint: disable=invalid-name
users = {'me@gmail.com': {'password': 'me@gmail.com', 'username': 'Mercy', 'email': 'me@gmail.com'}}

class User(object):
    """
    Class to handle  user functions
    """
    # pylint: disable-msg=C0103
    def __init__(self, username=None, email=None, password=None, cpassword=None):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password
        self.cpassword = cpassword

    def register(self, email, username, password, cpassword):
        """defining method to create account"""
        #check to make sure fields are not blank
        if username == '' or email == '' or password == '':
            msg = 'You have blank fields'
        else:
            regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            result = email
            if not re.match("[a-zA-Z0-9- .]+$", username):
                msg = "special characters in username"
            elif email in users.keys():
                msg = "email registered"
            elif not re.search(regex, result):
                msg = "invalid email"
            elif password != cpassword:
                msg = "password mismatch"
            elif len(password) < 6:
                msg = "password less than 6"
            else:
                users[email] = {
                    'username': username,
                    'email': email,
                    'password': password}
                return 1
            print(users.keys)
        return msg

    def login(self, email, password):
        """ defining method to validate user"""
        if email != '' and password != '':
            if email in users.keys():
                result = users[email]
                pword = result['password']
                if pword == password:
                    return 1
                return "password mismatch"
            return "not registered"
        return "blank fields"

    def get_user_name(self, email):
        """function to get a user's name"""
        if email in users.keys():
            result = users[email]
            return result['username']
        return False

    def get_user_email(self, email):
        """function to get a user's email"""
        if email in users.keys():
            result = users[email]
            return result['email']
        return False
        
