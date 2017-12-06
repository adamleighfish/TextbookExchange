from django.db import models
from django.contrib.auth.models import User

""" School Table

Standard db representation of a school
"""


class School(models.Model):
    school = models.CharField("school name", max_length=40, unique=False, default="")
    state = models.CharField("school state", max_length=2, unique=False, default="")
    city = models.CharField("school city", max_length=40, unique=False, default="")

    def __str__(self):
        return self.school


""" Student Table

Standard db representation of a student
"""


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    school = models.ForeignKey(School)
