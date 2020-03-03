from django.shortcuts import render

posts = [
    {
        'author': 'Mark Daniel Delgado',
        'title': 'First Ever Blog',
        'content': 'First Ever Content',
        'date_posted': 'March 2nd, 2020'
    },
    {
        'author': 'Mark Daniel Delgado',
        'title': 'Second Ever Blog',
        'content': 'First Ever Content for Second Post',
        'date_posted': 'March 2nd, 2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
