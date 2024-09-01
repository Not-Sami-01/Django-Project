from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email_or_phone = models.CharField(max_length=122)
    context = models.TextField()
    datetime = models.DateField()
    
    def __str__(self):
        return self.firstName

class UserLogins(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    datetime = models.DateField()

    def __str__(self):
        return self.username
    