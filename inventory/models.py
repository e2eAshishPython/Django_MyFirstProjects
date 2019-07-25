from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


# Create your models here.


class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('restaurant_detail', kwargs={'pk': self.pk})


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes',on_delete=models.CASCADE)

    
    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.restaurant.id})



class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)



