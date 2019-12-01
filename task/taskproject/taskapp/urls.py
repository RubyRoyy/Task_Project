from django.contrib import admin
from django.urls import path,include
from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    path('',views.UserListView.as_view()),
    path('signup/',views.SignUp.as_view()),
    path('login/',views.LoginView.as_view()),
    path('datedata/',views.DateData.as_view()),
    path('<str:username>/',views.ProfileUpdateView.as_view()),
 ]