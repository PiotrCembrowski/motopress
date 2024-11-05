from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect("press:login")
    else:
        form = AuthenticationForm()
    return render(request, 'press/login.html', { "form": form})