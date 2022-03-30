from django.db import models

# Create your models here.

class SuperAdmin(models.Model):
    SuperAdminId = models.AutoField(primary_key=True)
    SuperAdminName = models.CharField(max_length=500)
    SuperAdminEmail = models.CharField(max_length=500)
    SuperAdminPassword = models.CharField(max_length=500, default="abcd")


class Teacher(models.Model):
    TeacherId = models.AutoField(primary_key=True)
    TeacherName = models.CharField(max_length=500)
    TeacherEmail = models.CharField(max_length=500)
    TeacherPassword = models.CharField(max_length=500, default="abcd")

class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=500)
    StudentEmail = models.CharField(max_length=500)
    StudentPassword = models.CharField(max_length=500, default="abcd")

