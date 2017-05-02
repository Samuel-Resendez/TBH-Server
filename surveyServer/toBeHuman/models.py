from django.db import models

# Create your models here.

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()

    class Meta:
        ordering = ('created',)