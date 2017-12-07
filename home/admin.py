from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from home.models import Student, Book, Listing, Exchange, School


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(School)
admin.site.register(Book)
admin.site.register(Listing)
admin.site.register(Exchange)
admin.site.register(Student)
