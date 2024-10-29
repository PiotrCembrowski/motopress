from django.shortcuts import render

from press.models import Article

def frontpage(request):
    articles = Article.objects.all()
    return render(request, 'core/frontpage')

def contact(request):
    return render(request, 'core/contact')