from email.policy import default
from django.db import models
from store.models import *
# Create your models here.
class Juma_User(models.Model):
    user_email = models.TextField()
    user_name = models.CharField(max_length = 100)
    user_phone = models.BigIntegerField()
    user_rollno = models.TextField(default='191CS237', null=True)
    user_password = models.TextField()
    user_photo  = models.ImageField(upload_to = 'user_photos',default='photo')
    def __str__(self):
        return self.user_email


class Item_Type(models.Model):
    item_type = models.CharField(max_length = 100)
    item_photo = models.ImageField(upload_to = 'default_item_type_photos')
    def __str__(self):
        return self.item_type


class Item(models.Model):
    item_type = models.ForeignKey('Item_Type',on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 100)
    item_owner = models.ForeignKey('Juma_User',on_delete=models.CASCADE)
    item_price = models.PositiveIntegerField(default=0)
    item_description = models.TextField(default='')
    item_image = models.ImageField(upload_to = 'item_images',default='item_images/default.png')
    item_dispose = models.BooleanField(default=False)
    item_selling_status = models.BooleanField(default=False)
    def __str__(self):
        return self.item_name + str(self.item_price)


class Request(models.Model):
    item_type = models.ForeignKey('Item_Type',on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 100)
    item_buyer = models.ForeignKey('Juma_User',on_delete=models.CASCADE)
    item_max_price = models.PositiveIntegerField(default=0)
    item_description = models.TextField(default='')
    request_status = models.BooleanField(default=False)
    

class History(models.Model):
    item = models.ForeignKey('Item',on_delete=models.CASCADE)
    item_owner = models.ForeignKey('Juma_User',on_delete=models.CASCADE, related_name='item_owner')
    item_buyer = models.ForeignKey('Juma_User',on_delete=models.CASCADE, related_name='item_buyer')
    def __str__(self):
        return self.item+', '+self.item_owner+', '+self.item_buyer