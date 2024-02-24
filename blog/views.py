from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all()
    return render(request=request, template_name='blog/home.html', context={'posts': posts})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = PostForm()
    return render(request=request, template_name='blog/createPost.html', context={'form': form})


def read_post(request, post_id):
    if post_id:
        post = Post.objects.filter(pk=post_id)
    return render(request=request, template_name='blog/readPost.html', context={'post': post.get()})


def edit_post(request, post_id):
    if post_id:
        post = Post.objects.filter(pk=post_id).get()
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if not post:
                return HttpResponseForbidden("You are not authorized to perform this action.")
            else:
                if form.is_valid():
                    form.save()
                    return redirect("/read/{}".format(post.pk))
        else:
            form = PostForm(instance=post)
            return render(request=request, template_name='blog/updatePost.html', context={'form': form})
    return HttpResponseForbidden("You must provide a valid method and ID")


def delete_post(request, post_id):
    if post_id:
        no_more = Post.objects.filter(pk=post_id)
        if no_more.count() == 1:
            no_more.get().photo.delete(save=True)
            no_more.delete()
            return redirect('/')
    return HttpResponseForbidden("Insert a Post Before the Deletion!")
