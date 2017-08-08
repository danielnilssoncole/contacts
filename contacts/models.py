from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    # full_name = first_name + ' ' + last_name
    phone_number = models.IntegerField(default=0, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.full_name
