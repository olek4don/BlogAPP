from django.shortcuts import render
# from django.http import HttpResponse  # TODO: delete it

posts = [
    {
        'author': 'AxelEf',
        'title': 'Blog Post 1',
        'content': 'Content 1',
        'date_posted': 'December 23, 2022'
    },
    {
        'author': 'Ada J',
        'title': 'Blog Post 2',
        'content': 'Content 2',
        'date_posted': 'December 24, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')  # TODO: DELETE IT


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Blog'})
