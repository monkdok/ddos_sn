from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import PostCreateForm
from .models import Post, Like
from profiles.models import Profile


class PostListView(View):
    def get(self, request):
        post_form = PostCreateForm()
        posts = Post.objects.all()
        profile = Profile.objects.get(user=request.user)
        context = {
            'profile': profile,
            'posts': posts,
            'post_form': post_form,
        }
        return render(request, 'posts/post_list2.html', context)

    def post(self, request):
        form = PostCreateForm(request.POST, request.FILES)
        profile = Profile.objects.get(user=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = profile
            form.save()
            form = PostCreateForm()
        return redirect('posts:post_list_url')


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post.liked.all():
            post.liked.remove(profile)
        else:
            post.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
            post.save()
            like.save()
    return redirect('posts:post_list_url')

