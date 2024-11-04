from django.urls import path
from django.urls import include, path
from core.views import login

urlpatterns = [
    path('login/', login, name='login')
]
