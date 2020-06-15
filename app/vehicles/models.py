from django.db import models
from login.models import User
# Create your models here.


class Vehicle(models.Model):
    """ Vehicle Model """
    plate = models.CharField(max_length=6, unique=True,
                             blank=False, null=False)
    model = models.CharField(max_length=32, blank=False,
                             null=False)
    color = models.CharField(max_length=10, blank=False,
                             null=False)
    brand = models.CharField(max_length=24, blank=False,
                             null=False)
    user = models.ForeignKey(User, verbose_name=("user"),
                             on_delete=models.CASCADE,
                             null=False)

    class Meta:
        verbose_name = ("vehicle")
        verbose_name_plural = ("vehicles")

    def __str__(self):
        """ String Representation """
        return self.plate

    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"pk": self.pk})
