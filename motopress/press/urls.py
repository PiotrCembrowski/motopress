from django.urls import path
from press.views import login_view, post

app_name = 'press'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('post/', post, name='post'),
]
