from django.test import TestCase
from .models import Student
from faker import Faker

class StudentModelTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(name="Ahmed", age=20)
        self.assertEqual(student.name, "Ahmed")





# fake = Faker()

# for _ in range(999990):
#     name = fake.name()
#     email = fake.email()
#     address = fake.address()
#     age = fake.random_int(min=18, max=60)
#     phone = fake.phone_number()

#     student = Student.objects.create(name=name, email=email, address=address, age=age, phone=phone)