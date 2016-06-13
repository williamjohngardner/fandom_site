from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    image_src = models.URLField()
    desc = models.TextField()

    def __str__(self):
        return self.title
