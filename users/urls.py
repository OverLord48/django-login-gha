from django.urls import path
from users.views import *

urlpatterns = [
    path('auth/login', login.as_view())
]