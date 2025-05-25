from django.db import models
from django.db.models import DecimalField


class BookList(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    discount=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(null=True)
    photo=models.ImageField(upload_to='photo/',default=None)
    rate=models.DecimalField(max_digits=10,decimal_places=2)