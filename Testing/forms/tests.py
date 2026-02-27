from django.test import TestCase
from faker import Faker
from .models import MyModel

fake = Faker()

class MyModelTestCase(TestCase):
    def setUp(self):
        self.model = MyModel.objects.create(name=fake.name(),email=fake.email(),message=fake.text(),created_at = fake.date_time_between(start_date='-5y', end_date='now'))

    def test_model_creation(self):
        self.assertEqual(self.model.name, fake.name())
        self.assertEqual(self.model.email, fake.email())
        self.assertEqual(self.model.message, fake.text())
        self.assertEqual(self.model.created_at, fake.date_time_between(start_date='-5y', end_date='now'))

    def test_model_str(self):
        self.assertEqual(str(self.model), self.model.name)

    def test_model_update(self):
        self.model.name = fake.name()
        self.model.email = fake.email()
        self.model.message = fake.text()
        self.model.created_at = fake.date_time_between(start_date='-5y', end_date='now')
        self.model.save()
        self.assertEqual(self.model.name, fake.name())
        self.assertEqual(self.model.email, fake.email())
        self.assertEqual(self.model.message, fake.text())
        self.assertEqual(self.model.created_at, fake.date_time_between(start_date='-5y', end_date='now'))

    

if __name__ == '__main__':
    for i in range(1000):
        MyModel.objects.create(name=fake.name(),email=fake.email(),message=fake.text(),created_at = fake.date_time_between(start_date='-5y', end_date='now'))