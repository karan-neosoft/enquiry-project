from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Enquiry(models.Model):
    firstname = models.CharField(max_length=255,blank=False,null=False)
    lastname = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(validators=[EmailValidator(message="Enter correct email id ")],max_length=50, blank=False, null=False)
    service = models.CharField(max_length=30, blank=False, null=False)
    budget = models.FloatField(blank=False, null=False)
    message = models.CharField(max_length=450, blank=False, null=False)

    class Meta:
        db_table = 'enquiry_form'