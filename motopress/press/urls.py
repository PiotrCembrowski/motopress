from django.urls import path
from press.views import login

app_name = 'press'

urlpatterns = [
    path('press/login/', login, name='login')
]
