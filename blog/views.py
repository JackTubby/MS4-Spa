from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


def all_blogs(request):
    """ A view to return all blogs """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to show individual blog details """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """ Add a blog to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added a blog.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add a blog. Please make sure the form is valid!')
    else:
        form = BlogForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog.')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. Please make sure the form is valid!')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.name}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a treatment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted.')
    return redirect(reverse('home'))
