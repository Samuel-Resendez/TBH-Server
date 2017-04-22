from django.db import models

# Create your models here.

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    # The following should all be values between 1 - NumVals
    qOneResponse = models.IntegerField(default=1) #4
    qTwoResponse = models.IntegerField(default=1) #4
    qThreeResponse = models.IntegerField(default=1) #4
    qFourResponse = models.IntegerField(default=1) #5


    class Meta:
        ordering = ('created',)
