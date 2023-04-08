from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        ##Baraye inke file ha ruye hard niz zakhire shavad bayad hatman save shavad.

    def __str__(self):
        return self.title+str(self.created_date)
    ##Chon created_date str nist, ma un ro tabdil be str kardim