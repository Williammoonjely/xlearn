from django.db import models

# Create your models here.



class Account(models.Model):
    u_name = models.CharField(("User Name"), max_length=50)
    pwd = models.CharField(("Password"), max_length=50)
    role = models.CharField(("User Role"), max_length=50)
    
    
    def __str__(self):
        return self.u_name