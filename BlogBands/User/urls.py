from django.urls import path
from User.Views.authentication import Login, Logout



urlpatterns = [
    path('login/', Login.as_view(), name= 'Login'),
    path('logout/', Logout.as_view(), name= 'Logout'),
]
