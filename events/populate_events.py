import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arms_internship2.settings')

import django

django.setup()

# populate fake_script

import random
from events.models import Topic, WebPage, AccessRecords
from faker import Faker

fake_gen = Faker()

topics = ['Sports', 'Social', 'Religion', 'News', 'Education', 'Politics']


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]

    t.save()

    return t


# function to generate web pages and access records
def populate(n):
    for entry in range(n):
        top = add_topic()

        # create fake data
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        web_page = WebPage.objects.get_or_create(category=top, name=fake_name, url=fake_url)[0]

        acc_record = AccessRecords.objects.get_or_create(name=web_page, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating DB")
    populate(10)
    print('Done Populating DB')
