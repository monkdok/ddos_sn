import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import *



class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    liked = models.ManyToManyField(Profile, default=None, related_name='likes', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)


class Like(models.Model):
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike')
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateField(default=datetime.date.today)
    created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '{}-{}'.format(self.user, self.post, self.value)

    def get_like_num(self):
        return self.post_set.count()

    def save(self, *args, **kwargs):
        # date = datetime.datetime.strptime(str(self.created), "%Y-%m-%d")
        date = datetime.date.today()
        self.created = date
        super(Like, self).save(*args, **kwargs)
