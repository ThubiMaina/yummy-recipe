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
    def __init__(self, username = None, email = None, password= None, cpassword=None):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password
        self.cpassword = cpassword
        
    def register(self, email, username, password, cpassword):
        """defining method to create account"""
        if username != '' and email != '' and password != '':    
            if re.match("[a-zA-Z0-9- .]+$",username):
                if email not in users.keys():
                    if username not in users.keys():
                        if password == cpassword:
                            regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                            result = email
                            if re.search(regex, result):
                                if len(password) < 6:
                                
                                
                                    users[email] = {
                                        'username': username,
                                        'email': email,
                                        'password': password,
                                    }
                        
                                    print(users.keys)
                                    return 1
                                return "password less than 6"       
                            return "invalid email"
                        return "password mismatch"
                    return "username exists"
                return "email registered"
            return "special characters in username"
        return "blank fields"

    def login(self, email, password):
        """ defining method to validate user"""
        if email != '' and password != '':
            if email in users.keys():
                result = users[email]
                pword = result['password']
                if pword == password:
                    return 1
                return 2 
            return 3 
        return 4 

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
