from django.db import models

PRODUCT = 'Product'
SERVICE = 'Service'
TYPE_SUBCATEGORY_CHOICES = (
    (PRODUCT, 'Product'),
    (SERVICE, 'Service'),
)

class Category(models.Model):
    name = models.CharField(max_length=255)
    type_category = models.CharField(max_length=255, choices=TYPE_SUBCATEGORY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
