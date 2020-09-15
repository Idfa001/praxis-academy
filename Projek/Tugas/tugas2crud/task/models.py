from django.db import models

class Task(models.Model):
    name = models.TextField()

class customer(models.Model):
    customername = models.TextField(default='')
    customeraddress = models.TextField(default='')
    customercontact = models.TextField(default='')

class supplier(models.Model):
    suppliername = models.TextField(default='')
    supplieraddress = models.TextField(default='')
    suppliercontact = models.TextField(default='')

class item(models.Model):
    itemname = models.TextField(default='')
    itemprice = models.IntegerField(default=0)
    itemsaleprice = models.IntegerField(default=0)
