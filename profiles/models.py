from django.contrib.auth.models import User
from django.db import models
# from django.utils.text import slugify
# from slugify import slugify
from django.template.defaultfilters import slugify
from datetime import date

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


