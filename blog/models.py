from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name
