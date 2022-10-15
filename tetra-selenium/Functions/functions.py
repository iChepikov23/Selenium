import os
import random
import string


class FunctionsUtils:

    def __init__(self):
        self.random = format(random.randint(0000, 999999), '04d')
        self.prefix = 'Jose'
        self.prefix_regression = 'jose.luis+regression'
        self.domain = 'tetra.team'
        self.organization = 'Organization'
        self.bad_password = '126788'
        self.image = 'profile.png'
        self.project = 'Project_'
        self.accounts = 'accounts.xlsx'

    # random
    def generate_random(self):
        return self.random

    # email random
    def generate_email(self, number):
        email = self.prefix_regression + number + '@' + self.domain
        return email

    def generate_email_invite(self, number):
        email = self.prefix_regression + number + '@' + self.domain
        return email

    # email random
    def generate_error_email(self):
        return self.prefix + self.domain

    # Organization random
    def generate_organization(self, number):
        return self.organization + number

    # name random
    def generate_name(self, number):
        return self.prefix + number

    # name random
    def generate_full_name(self, number):
        return self.prefix + number

    def generate_project_name(self, number):
        return self.project + number

    def get_profile_photo(self):
        # get new account create
        directory = os.path.dirname(__file__)
        directory = directory.replace('Functions', 'data')
        return os.path.join(os.path.sep, directory, self.image)

    def generate_password(self):
        chars = string.ascii_uppercase
        chars1 = string.digits
        chars2 = '!'
        chars3 = string.ascii_lowercase
        return ''.join((random.choice(chars) + random.choice(chars1)
                        + random.choice(chars2) + random.choice(chars3)) for x in range(4))

    def generate_bad_password(self):
        return self.bad_password
