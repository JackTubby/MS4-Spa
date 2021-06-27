from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Treatment(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    amount = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    RATE_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Average'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=3)
    time_added = models.DateTimeField(default=timezone.now)
    readonly_fields = ['treatment', 'user', 'time_added']

    def __str__(self):
        return self.user.username
