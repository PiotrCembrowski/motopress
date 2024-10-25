from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage')

def contact(request):
    return render(request, 'core/contact')