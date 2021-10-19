from django.db import models
from model_utils import Choices


class Register(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    pincode = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=10,default='India')

class Books(models.Model):
    def __str__(self):
        return self.name

    STATUS = Choices('available', 'given')
    CONDITION = Choices('good','okay','bad')
    CLASS = Choices('1','2','3','4','5','6','7','8','9','10','11','12')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    book_class = models.CharField(max_length=2,choices=CLASS)
    publisher = models.CharField(max_length=45)
    cover_pic = models.ImageField(default='default.png',upload_to='media/book_images')
    edition_year = models.CharField(max_length=4)
    price = models.IntegerField()
    condition = models.CharField(max_length=10,choices=CONDITION)
    status = models.CharField(max_length=15,choices=STATUS)
    insert_date = models.DateField(blank=True,null=True)

    
