from django.urls import path
from . import views
from .views import TaskCreateView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_list, name='task-list'),
  #  path('create/', views.create_task, name='create-task'),
    path('create/', TaskCreateView.as_view(), name='create-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('update/<int:pk>/', views.update_task, name='update-task'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]