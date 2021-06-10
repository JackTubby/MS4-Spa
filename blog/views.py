from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    """ A view to return all treatments, including sorting and search quries """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)
