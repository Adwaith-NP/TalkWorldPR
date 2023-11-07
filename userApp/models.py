from django.db import models

# Create your models here.

class chatInfo(models.Model):
    userName = models.CharField(max_length=20,unique=False)
    senderName = models.CharField(max_length=20,unique=False)
    userMessage = models.TextField(max_length=100,unique=False)
    
    def __str__(self):
        return self.userName
    
class addlist(models.Model):
    username = models.CharField(max_length=20,unique=False)
    addedUserName = models.CharField(max_length=20,unique=False)
    
    def __str__(self):
        return self.username
