from django.contrib import messages
from django.core import mail
from django.conf import settings
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
# from .models import User, Retailer
import random
import requests as r

from .models import Student, Teacher, SuperAdmin



from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

def post(self, request, *args, **kwargs):
    self.http_method_names.append("post")
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })




def welcome(request, *args, **kwargs):
    return render(request, 'home.html')

def student(request, *args, **kwargs):
    return render(request, 'student.html')

def teacher(request, *args, **kwargs):
    return render(request, 'teacher.html')

def superAdmin(request, *args, **kwargs):
    return render(request, 'admin.html')

def listStudents(request, *args, **kwargs):
    liststudent = Student.objects.all()
    context = {
        "liststudents": liststudent
    }
    return render(request, 'listStudent.html', context=context)

def listTeachers(request, *args, **kwargs):
    listTeachers = Teacher.objects.all()
    context = {
        "listTeachers": listTeachers
    }
    return render(request, 'listTeachers.html', context=context)


def studentLogin(request, *args, **kwargs):
    return render(request, 'loginStudent.html')

def studentRegister(request, *args, **kwargs):
    return render(request, 'registerStudent.html')

def teacherLogin(request, *args, **kwargs):
    return render(request, 'loginTeacher.html')

def teacherRegister(request, *args, **kwargs):
    return render(request, 'registerTeacher.html')

def superAdminLogin(request, *args, **kwargs):
    return render(request, 'loginAdmin.html')

def superAdminRegister(request, *args, **kwargs):
    return render(request, 'registerAdmin.html')

def studentLogin1(request, *args, **kwargs):
    email = request.POST.get('email')
    password = request.POST.get('password')
    userlist = Student.objects.filter(StudentEmail=email).values()

    if len(userlist) > 0:
        userA = userlist[0]
        if password == userA['StudentPassword']:
            # if password == userA['password']:
            # print(userA['name'])
            context = {
                "userid": email,
                "user": userA['StudentName']
            }
            request.session['eid'] = userA['StudentId']
            # return render(request, 'index_mainpage.html', {'userMain': userA['name']})
            return render(request, 'student.html', context=context)
            # return redirect('../home/', {'userMain': userA['name']})

        else:
            messages.info(request, 'Wrong password')
            return render(request, 'loginStudent.html', context={"message":'Wrong password'})

    else:
        messages.info(request, 'User is not registered')
        return render(request, 'loginStudent.html', context={"message":'User is not registered'})


def studentRegister1(request, *args, **kwargs):
    Name = request.POST.get('Name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')

    userlist = Student.objects.filter(StudentEmail=email).values()
    if (len(userlist) == 0):
        if password != password1:
            messages.info(request, "Password does not match")
            return render(request, 'registerStudent.html', context={"message":"Password does not match"})
        else:
            # P = make_password(password)
            a = Student()
            a.StudentName = Name
            a.StudentEmail = email
            a.StudentPassword = password
            a.save()
            context = {
                "userid": email,
                "user": Name
            }
            messages.info(request, "You are now signed up Try to login")
            return render(request, 'student.html', context=context)
    else:
        messages.info(request, "User already registered")
        return render(request, 'registerStudent.html', context={"message":"User already registered"})

def teacherLogin1(request, *args, **kwargs):
    email = request.POST.get('email')
    password = request.POST.get('password')
    userlist = Teacher.objects.filter(TeacherEmail=email).values()

    if len(userlist) > 0:
        userA = userlist[0]
        if password == userA['TeacherPassword']:
            # if password == userA['password']:
            # print(userA['name'])
            context = {
                "userid": email,
                "user": userA['TeacherName']
            }
            request.session['eid'] = userA['TeacherId']
            # return render(request, 'index_mainpage.html', {'userMain': userA['name']})
            return render(request, 'teacher.html', context=context)
            # return redirect('../home/', {'userMain': userA['name']})

        else:
            messages.info(request, 'Wrong password')
            return render(request, 'loginTeacher.html', context={"message":'Wrong password'})

    else:
        messages.info(request, 'User is not registered')
        return render(request, 'loginTeacher.html', context={"message":'User is not registered'})


def teacherRegister1(request, *args, **kwargs):
    Name = request.POST.get('Name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')

    userlist = Teacher.objects.filter(TeacherEmail=email).values()
    if (len(userlist) == 0):
        if password != password1:
            messages.info(request, "Password does not match")
            return render(request, 'registerTeacher.html', context={"message":"Password does not match"})
        else:
            # P = make_password(password)
            a = Teacher()
            a.TeacherName = Name
            a.TeacherEmail = email
            a.TeacherPassword = password
            a.save()
            context = {
                "userid": email,
                "user": Name
            }
            messages.info(request, "You are now signed up Try to login")
            return render(request, 'teacher.html', context=context)
    else:
        messages.info(request, "User already registered")
        return render(request, 'registerTeacher.html', context={"message":"User already registered"})


def superAdminLogin1(request, *args, **kwargs):
    email = request.POST.get('email')
    password = request.POST.get('password')
    userlist = SuperAdmin.objects.filter(SuperAdminEmail=email).values()

    if len(userlist) > 0:
        userA = userlist[0]
        if password == userA['SuperAdminPassword']:
            # if password == userA['password']:
            # print(userA['name'])
            context = {
                "userid": email,
                "user": userA['SuperAdminName']
            }
            request.session['eid'] = userA['SuperAdminId']
            # return render(request, 'index_mainpage.html', {'userMain': userA['name']})
            return render(request, 'admin.html', context=context)
            # return redirect('../home/', {'userMain': userA['name']})

        else:
            messages.info(request, 'Wrong password')
            return render(request, 'loginAdmin.html', context={"message":'Wrong password'})

    else:
        messages.info(request, 'User is not registered')
        return render(request, 'loginAdmin.html', context={"message":'User is not registered'})


def superAdminRegister1(request, *args, **kwargs):
    Name = request.POST.get('Name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')

    userlist = SuperAdmin.objects.filter(SuperAdminEmail=email).values()
    if (len(userlist) == 0):
        if password != password1:
            messages.info(request, "Password does not match")
            return render(request, 'registerAdmin.html', context={"message":"Password does not match"})
        else:
            # P = make_password(password)
            a = SuperAdmin()
            a.SuperAdminName = Name
            a.SuperAdminEmail = email
            a.SuperAdminPassword = password
            a.save()
            context = {
                "userid": email,
                "user": Name
            }
            messages.info(request, "You are now signed up Try to login")
            return render(request, 'admin.html', context=context)
    else:
        messages.info(request, "User already registered")
        return render(request, 'registerAdmin.html', context={"message":"User already registered"})