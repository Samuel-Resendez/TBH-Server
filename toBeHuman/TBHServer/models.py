from django.db import models

# Create your models here.

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=true)
    

    class Meta:
        ordering = ('created')
