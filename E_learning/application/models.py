from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms.fields import CharField

class ContactUs(models.Model):
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    phone=models.IntegerField()
    msg = models.CharField(max_length=100)




class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    user_img = models.ImageField(upload_to='user_images',default='/profilePic.png')

def __str__(self):
    return f'{self.user} Profile'



class Course(models.Model):
    title = models.CharField(max_length=100)
    company= models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    price = models.FloatField()
    course_img = models.ImageField(upload_to='courseimg')
    types = models.CharField(max_length=100,default='not avaliable')

def __str__(self):
    return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

def __str__(self):
    return str(self.id)

class CourseBought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bcourse = models.ForeignKey(Course, on_delete=models.CASCADE)

def __str__(self):
    return str(self.id)




class Internship(models.Model):
    intern_title = models.CharField(max_length=70)
    intern_subtitle = models.CharField(max_length=70)
    company_img = models.ImageField(upload_to='internship_Company')
    intern_location = models.CharField(max_length=70)
    intern_start_date = models.CharField(max_length=70)
    intern_duration = models.CharField(max_length=70)
    intern_stipen = models.IntegerField()
    intern_last_date = models.CharField(max_length=70)
    intern_or_part_time = models.CharField( max_length=70)


class intership_apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)


def __str__(self):
    return str(self.id)




class Job(models.Model):
    job_offer = models.CharField(max_length=50)
    job_des = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    job_comp_img = models.ImageField(upload_to='job_company')
    job_comp_name = models.CharField(max_length=50, default=1)
    job_t_left = models.CharField(max_length=50)
    

def __str__(self):
    return str(self.id)

class job_display(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

