from django.db import models

# Create your models here.
 
class Application(models.Model):
    f_name = models.CharField(("First Name"), max_length=50)
    l_name = models.CharField(("Last Name"), max_length=50)
    mobile_no = models.IntegerField(("Mobile Number"))
    email_add = models.EmailField(("Email Address"), max_length=254)
    edu_qual = models.CharField(("Eduaction Qualification"), max_length=50)
    
    def __str__(self):
        return self.f_name
    
    
