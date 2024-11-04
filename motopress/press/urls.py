from django.urls import path
from press.views import login

app_name = 'press'

urlpatterns = [
    path('login/', login, name='login')
]
