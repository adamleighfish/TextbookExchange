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


""" Book Table

Standard db representation of a book
"""


class Book(models.Model):
    ISBN = models.IntegerField(default="")
    title = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.title


""" Listing Table

A listing of a book by a student.
Field type indicates whether is book the student is listing is one he/she wants(W) or is giving(G).
"""


class Listing(models.Model):
    TYPES = (
        ('W', 'Want'),
        ('G', 'Give'),
    )
    sid = models.ForeignKey(Student, on_delete=models.CASCADE)
    bid = models.ForeignKey(Book, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField(auto_now_add=True)
    open = models.BooleanField(default=True)


""" Exchange Table

An exchange of books between two students.
Field bid1 represents the book sid1 is giving away and vice versa with bid2/sid2
"""


class Exchange(models.Model):
    sid1 = models.ForeignKey(Student, related_name='+', on_delete=models.CASCADE)
    bid1 = models.ForeignKey(Book, related_name='+', on_delete=models.CASCADE)
    sid2 = models.ForeignKey(Student, related_name='+', on_delete=models.CASCADE)
    bid2 = models.ForeignKey(Book, related_name='+', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
