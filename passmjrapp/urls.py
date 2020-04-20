from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('view/<str:pk>/', views.view, name='view'),

    path('passwordcreate/', views.passwordcreate, name='passwordcreate'),
    path('passgenerate/', views.passgenerate, name='passgenerate'),


]
