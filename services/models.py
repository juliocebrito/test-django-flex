from django.db import models
from categories.models import Category
from subcategories.models import Subcategory

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name='services')
    subcategory = models.ForeignKey(Subcategory, related_name='services')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.name
