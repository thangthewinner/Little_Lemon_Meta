from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self) -> str:
        return self.name 
    
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name