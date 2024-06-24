from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=300)
    image=models.ImageField(upload_to='image/')
    price=models.FloatField()
    description=models.TextField()


    def __str__(self):
        return self.name