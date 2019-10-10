from django.shortcuts import render


posts = [
    {
        'author': 'Tiago',
        'title': 'Hello World',
        'content': 'Post text Post text',
        'date_posted': 'October 09, 2019',
    },
    {
        'author': 'Tiago',
        'title': 'Bye world',
        'content': 'Post text Post text',
        'date_posted': 'October 10, 2019',
    },
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})