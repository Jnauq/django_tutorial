from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Tom Hanks',
        'title': 'Blog post 1',
        'content': 'Testing first post!',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Michael B Jordan',
        'title': 'Hey blog!',
        'content': 'Testing blog app!',
        'date_posted': 'November 1, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })
