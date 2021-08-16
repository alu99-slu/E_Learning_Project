from django.contrib import admin
from .models import (ContactUs,Course,Cart,Customer,
Internship,intership_apply, CourseBought, Job,job_display)


@admin.register(Customer)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_img']

@admin.register(ContactUs)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone','msg')

@admin.register(Course)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'company',
                    'duration', 'level', 'price', 'course_img']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']


@admin.register(CourseBought)
class boughtCourseModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'bcourse']

@admin.register(Internship)
class IntershipModelAdmin(admin.ModelAdmin):
    list_display = ['intern_title', 'intern_subtitle',
                    'company_img', 'intern_location', 'intern_start_date',
                    'intern_duration', 'intern_stipen','intern_last_date',
                    'intern_or_part_time']

@admin.register(intership_apply)
class internship_applyModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'internship']

@admin.register(Job)
class jobModelAdmin(admin.ModelAdmin):
    list_display = ['job_offer', 'job_des',
                    'job_location', 'job_comp_img', 'job_comp_name',
                    'job_t_left']

@admin.register(job_display)
class jobDisplayModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'job']
