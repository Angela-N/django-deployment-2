import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arms_internship2.settings')

import django

django.setup()

# populate fake_script

import random
from users.models import UserModel
from faker import Faker

fake_gen = Faker()


# function to generate web pages and access records
def populate(n=5):
    for entry in range(n):
        name = fake_gen.name().split()
        fake_first_name = name[0]
        fake_last_name = name[1]
        fake_email = fake_gen.email()

        user = UserModel.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating DB")
    populate()
    print('Done Populating DB')
