from django.test import TestCase
from .models import User
from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        today = timezone.now()
        User.objects.create(username="user5", birth_date=today - relativedelta(years=20))
        User.objects.create(username="user6", birth_date=today - relativedelta(years=9))
        User.objects.create(username="user7", birth_date=today - relativedelta(years=13, days=-1))
        User.objects.create(username="user8", birth_date=today - relativedelta(years=13, days=1))
        User.objects.create(username="user9", birth_date=today - relativedelta(years=13))

        User.objects.create(username="user10", random_number ="33")
        User.objects.create(username="user11", random_number="50")
        User.objects.create(username="user12", random_number="30")
        User.objects.create(username="user13", random_number="13")

    def test_calculateAge(self):
        user5 = User.objects.get(username="user5")
        user6 = User.objects.get(username="user6")
        user7 = User.objects.get(username="user7")
        user8 = User.objects.get(username="user8")
        user9 = User.objects.get(username="user9")
        self.assertEqual(user5.calculateAge(), 'allowed')
        self.assertEqual(user6.calculateAge(), 'blocked')
        self.assertEqual(user7.calculateAge(), 'blocked')
        self.assertEqual(user8.calculateAge(), 'allowed')
        self.assertEqual(user9.calculateAge(), 'blocked')

    def test_BizzFuzz(self):
        user10 = User.objects.get(username="user10")
        user11 = User.objects.get(username="user11")
        user12 = User.objects.get(username="user12")
        user13 = User.objects.get(username="user13")
        self.assertEqual(user10.BizzFuzz(), 'Bizz')
        self.assertEqual(user11.BizzFuzz(), 'Fuzz')
        self.assertEqual(user12.BizzFuzz(), 'BizzFuzz')
        self.assertEqual(user13.BizzFuzz(), 13)


