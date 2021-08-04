from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField


def emptylist():
    return []


class ProPic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')
    mobile = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.first_name


departments = [('Two wheeler', 'Two wheeler'),
               ('Three wheeler', 'Three wheeler'),
               ('Four wheeler', 'Four wheeler'),
               ]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    driver = models.BooleanField(default=False)
    vehicle = models.CharField(max_length=20, blank=True, choices=departments, default='Four wheeler')
    plate = models.CharField(max_length=30, blank=True)
    capacity = models.IntegerField(default=1, validators=[MaxValueValidator(200), MinValueValidator(1)])
    special = models.CharField(max_length=200, blank=True, default='')
    otp = models.CharField(default='no otp', max_length=20)


all_places = open('users/new.txt').readlines()
destinations = [(i, i) for i in all_places]


######

class Ride(models.Model):
    status = models.CharField(max_length=10, default='open')
    source = models.CharField(max_length=50, blank=False, choices=destinations, default='Aakkulam')
    destination = models.CharField(max_length=50, blank=False, choices=destinations)
    arrivaldate = models.DateTimeField()
    passenger = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(1)])
    sharable = models.BooleanField(default=False)
    vehicle = models.CharField(max_length=20, blank=True)
    special = models.CharField(max_length=200, blank=True)
    pets_allowed = models.BooleanField(default=False, blank=True)
    liguor_allowed = models.BooleanField(default=False, blank=True)
    play_music = models.BooleanField(default=False, blank=True)
    no_smoking = models.BooleanField(default=False, blank=True)
    female_only = models.BooleanField(default=False, blank=True)
    male_only = models.BooleanField(default=False, blank=True)
    driver_id = models.IntegerField(default=-1, blank=True)
    rider_id = models.IntegerField(default=-1, blank=False)
    rider_mobile = models.CharField(max_length=10, default='1234567890')
    sharer_id = ArrayField(models.IntegerField(), default=emptylist)
    sharer_passenger = ArrayField(models.IntegerField(), default=emptylist)
    total_psg = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(1)], default=0)

    def __str__(self):
        return f'{self.destination} on {str(self.arrivaldate)[:16]}'

class Review(models.Model):
    pic = models.FileField(upload_to='reviewPics', null=True, default=False)
    name = models.CharField(max_length=30, default=False)
    review = models.CharField(max_length=300)
    rating = models.IntegerField(default=4, validators=[MinLengthValidator(0), MaxValueValidator(5)])