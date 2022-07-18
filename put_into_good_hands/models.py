from django.contrib.auth.models import User
from django.db import models

TYPES = (
    (1, "Fundacja"),
    (2, "Organizacja pozarządowa"),
    (3, "Zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=64)

    @property
    def call(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.call


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    @property
    def call(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.call


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.BigIntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
