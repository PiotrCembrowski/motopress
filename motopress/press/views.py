from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("press:login")
    else:
        form = AuthenticationForm()
    return render(request, 'press/login.html', { "form": form})

@login_required(login_url="/press/login/")
def post(request):
    return render(request, 'press/post.html')