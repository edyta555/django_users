from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.utils import timezone

def random_number_1_100():
    return str(random.randint(1, 100))

# Create your models here.
class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    random_number = models.IntegerField(default=random_number_1_100)

    def calculateAge(self):
        today = timezone.now()
        age = today.year - self.birth_date.year \
              - ((today.month, today.day) <= (self.birth_date.month, self.birth_date.day))

        if age >= 13:
            return "allowed"
        else:
            return "blocked"

    def BizzFuzz(self):
        if self.random_number % 3 == 0:
            if self.random_number % 5 == 0:
                return "BizzFuzz"
            else:
                return "Bizz"
        elif self.random_number % 5 == 0:
            return "Fuzz"
        else:
            return self.random_number