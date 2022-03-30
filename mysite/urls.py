"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restcheck import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('superAdmin/', views.superAdmin),
    path('teacher/', views.teacher),
    path('student/', views.student),
    path('student/login/', views.studentLogin),
    path('student/register/', views.studentRegister),
    path('student/loginpath/', views.studentLogin1),
    path('student/registerpath/', views.studentRegister1),

    path('teacher/login/', views.teacherLogin),
    path('teacher/register/', views.teacherRegister),
    path('teacher/loginpath/', views.teacherLogin1),
    path('teacher/registerpath/', views.teacherRegister1),

    path('superAdmin/login/', views.superAdminLogin),
    path('superAdmin/register/', views.superAdminRegister),
    path('superAdmin/loginpath/', views.superAdminLogin1),
    path('superAdmin/registerpath/', views.superAdminRegister1),

    path('studentList/', views.listStudents),
    path('teacherList/', views.listTeachers),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
]

# from django.urls import path

# urlpatterns = [
#     path('api/register/', RegisterAPI.as_view(), name='register'),
# ]