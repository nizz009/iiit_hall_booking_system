from django.contrib import admin
from .models import User, Student, Admin, Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Profile)