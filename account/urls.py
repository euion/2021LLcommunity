from django.urls import path
from account import views

app_name = 'login'

urlpatterns = [
    # get login/ -> token, redirect index/
    path('login/', views.login, name="login"),
    # get signup/, post signup/ -> redirect login/
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
]