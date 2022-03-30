from django.contrib import admin

# Register your models here.
from .models import SuperAdmin, Teacher, Student

admin.site.register(SuperAdmin)
admin.site.register(Teacher)
admin.site.register(Student)