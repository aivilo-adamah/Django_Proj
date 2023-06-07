from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

STATE_CHOICES=(
    ('Accra', 'GHANA'),
    ('Lagos', 'NIGERIA'),
    ('Johannesburg', 'AFRIQUE DU SUD'),
    ('Niamey', 'NIGER'),
    ('Nairobi', 'KENYA'),
    ('Rabat', 'MAROC'),
    ('Alger', 'ALGÉRIE'),
    ('Caire', 'EGYPTE'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField(default='')
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    locality=models.CharField(max_length=70)
    city=models.CharField(max_length=80)
    mobile=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES, max_length=100)
    zipcode=models.IntegerField()
    def __str__(self):
        return self.name
    
    
