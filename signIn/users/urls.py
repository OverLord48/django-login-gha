from django.urls import path
from users.views import *

urlpatterns = [
    path('auht/signup', SignupView.as_view()),
    path('auth/signin', login.as_view()),
    path('auth/logout', LogoutView.as_view())
]