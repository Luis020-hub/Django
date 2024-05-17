from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('create/', views.student_create, name='student_create'),
    path('edit/<str:matricula>/', views.student_edit, name='student_edit'),
    path('delete/<str:matricula>/', views.student_delete, name='student_delete'),
]
