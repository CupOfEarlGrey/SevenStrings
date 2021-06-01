from django.db import models
from django.urls import reverse
# Create your models here.
electric_guitar = "Electric Guitar"
acoustic_guitar = 'Acoustic Guitar'
accessories = "Accessories"
ProductCategory = [
    (electric_guitar, "Electric Guitar"),
    (acoustic_guitar, "Acoustic Guitar"),
    (accessories, "Accessories")
]


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    brand = models.CharField(max_length=100, default=None)
    image = models.ImageField(upload_to='main_seven_strings/media/&Y/', blank=True)
    image_2 = models.ImageField(upload_to='main_seven_strings/media/&Y/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    category = models.CharField(max_length=100, choices=ProductCategory, default="Electric Guitar")

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main_seven_strings:product_detail", args=[self.id, self.slug])


