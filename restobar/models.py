from django.db import models
import datetime



# Create your models here.

class Team(models.Model):
    Name = models.CharField(max_length=200,default="" ,unique=True)
    pic = models.ImageField(upload_to='images',default="")
    DesCrip = models.TextField(default="")

    def __str__(self):
        return self.Name


class Menu(models.Model):
    Name = models.CharField(max_length=200,default='')
    menu_type = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.Name

class menu_item(models.Model):
    Name = models.CharField(max_length=200,default='')
    Pic = models.ImageField(upload_to='images',default="")
    Description = models.TextField(default="")
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    MainMenuType = models.ForeignKey(Menu,related_name='menu_items' , on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Food_Type(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Occasion(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
  

class Reservations(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField() 
    ContectNo = models.CharField(max_length=200)
    No_Of_person = models.IntegerField()
    Date = models.DateField(("Date"), default=datetime.date.today)
    Time = models.TimeField()
    
    preferred_food = models.ForeignKey(Food_Type,related_name="Foods" , on_delete=models.CASCADE)
    Occasion = models.ForeignKey(Occasion,related_name="Occasions" , on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name



