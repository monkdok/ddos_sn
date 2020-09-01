from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from rest_framework.response import Response

from .utils import get_random_code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, unique=False)
    last_name = models.CharField(max_length=100, blank=True, unique=False)
    # gender = models.BooleanField()
    country = models.CharField(max_length=40, blank=True, unique=False)
    bio = models.TextField(max_length=400, blank=True, default='no bio...')
    email = models.EmailField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatars/avatar.png', upload_to='avatars/')
    # friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_posts_num(self):
        # "posts" related_name of field "author" in the Post model
        return self.posts.all().count()

    def get_authors_posts(self):
        return self.posts.all()

    def get_likes_given_num(self):
        likes = self.like_set.all()
        total_liked = 0
        for like in likes:
            if like.value == 'Like':
                total_liked += 1
        return total_liked

    def get_likes_receive_num(self):
        posts = self.posts.all()
        total_liked = 0
        for post in posts:
            total_liked += post.liked.all().count()
        return total_liked

    def __str__(self):
        return '{}-{}'.format(self.user.username, self.created.strftime('%d-%m-%Y'),)

    def save(self, *args, **kwargs):
        exist = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + ' ' + str(self.last_name))

            # exist() function returns False or True
            exist = Profile.objects.filter(slug=to_slug).exists()
            while exist:
                to_slug = slugify(to_slug + ' ' + str(get_random_code()))
                exist = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

