from django.db import models
from django.utils import timezone

class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice_topic=models.CharField(max_length=45)
    notice_content= models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):#represent object in the form of string
        return self.notice_topic



class Course_Detail(models.Model):
    course_name = models.CharField(max_length=45,primary_key=True)
    duration=models.CharField(max_length=45,null=False,default="1Year")
    fees=models.IntegerField(default=0,null=False)
    description=models.TextField(null=True)
    def __str__(self):#represent object in the form of string
        return self.course_name

class Contact(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    your_query=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):#represent object in the form of string
        return self.name

class Job(models.Model):
    job_designation= models.CharField(max_length=100,default="",null=False)
    no_of_seats=models.IntegerField(default=0)
    last_date_to_apply=models.DateField(null=False,default=timezone.now)
    posted_date=models.DateField(default=timezone.now)
    reply_email=models.EmailField(max_length=55,default="",null=False)
    def __str__(self):#represent object in the form of string
        return self.job_designation

class User_Feedback(models.Model):
    name=models.CharField(max_length=45,default="",null=False)
    ratings=models.IntegerField(default=1)
    review_text=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Consultancy(models.Model):
    user_id=models.CharField(max_length=45,primary_key=True)
    paasword=models.CharField(max_length=50)
    name=models.CharField(max_length=45,default="")
    email=models.EmailField(max_length=45,)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=45)
    address=models.TextField()
    date=models.DateField(default=timezone.now)

class AdministrativeStaff(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    designation=models.CharField(max_length=100,null=False)
    experience=models.CharField(max_length=45,null=False)
    pic_name=models.FileField(max_length=100,upload_to="college/picture",default="")
    def __str__(self):
         return self.name


############### how to make a form using model###############

class Enquiry(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10)
    query=models.TextField()
    def __str__(self):
        return self.name