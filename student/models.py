from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student_Details(models.Model):
    student=models.OneToOneField(User,null=False, on_delete=models.DO_NOTHING)
    phone=models.CharField(max_length=10,null=False,default='')
    city=models.CharField(max_length=10,null=False,default='')
    address=models.TextField()

# class Edit_Profile(models.Model):
#     edit=models.OneToOneField(User,null=False, on_delete=models.DO_NOTHING)
#     email=models.EmailField(max_length=40,null=False,default='')
#     first_name=models.CharField(max_length=45,null=False,default='')
#     last_name=models.CharField(max_length=45,null=False,default='')