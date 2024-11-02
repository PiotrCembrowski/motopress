from django.shortcuts import render

from press.models import Article

def frontpage(request):
    articles = Article.objects.all()
    return render(request, 'core/frontpage.html', {'articles': articles})

def contact(request):
    return render(request, 'core/contact.html')

def post(request):
    return render(request, 'core/post.html')

def article(request):
    return render(request, 'core/article.html')