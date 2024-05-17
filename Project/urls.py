"""
URL configuration for Project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from puc_student.views import login_page, student_list, student_create, student_edit, student_delete, search_students

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('student/list/', student_list, name='student_list'),
    path('student/create/', student_create, name='student_create'),
    path('student/edit/<str:matricula>/', student_edit, name='student_edit'),
    path('student/delete/<str:matricula>/', student_delete, name='student_delete'),
    path('search/', search_students, name='search_students'),
]
