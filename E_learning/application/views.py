from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import FeebbackForm
from .models import ContactUs, Course , Cart ,Internship, intership_apply, job_display ,Job , Course_which_Bought
from .authinticationform import singUpform, logInform, userEditForm, UserProfileImage
from django.contrib import messages
from django.views import View
from .models import Customer

def application_home(request):
    return render(request,'home/home.html')

def application_about(request):
    return render(request,'about/about.html')

# def filter_course(request, data=None):
#     if data == None:
#         courses = Course.objects.filter(category='C')
#     elif data=='ch' or data =='hs' or data=='clg' or data=='ext':
#         courses = Course.objects.filter(category='C').filter(brand=data)
#     return render(request,'course/filterCourse.html',{'course':courses})

class CourseView(View):
    def get(self,request):
        course = Course.objects.all()
        return render(request, 'course/course.html', {'course': course})

class BuyCourse(View):
    def get(self,request,pk):
        course_list = Course.objects.get(pk=pk)
        return render(request, 'course/buycourse.html',{'course_list':course_list})

def buycourse(request):
    user = request.user
    course_id = request.GET.get('prod_id')
    course = Course.objects.get(id=course_id)
    Cart(user=user,course=course).save()
    return redirect('/profile')

# def coursebuy(request):
#     user = request.user
#     course_id = request.GET.get('buy_course')
#     course = Course.objects.get(id=course_id)
#     Course_which_Bought(user=user,buy_course=course).save()
#     return redirect('/profile')

# def cartCourses(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             user = request.user
#             cart = Course_which_Bought.objects.filter(user=user)
#         else:
#             user = request.user
#             cart = Course_which_Bought.objects.filter(user=user)
#             print(cart)
#         return render(request, 'course/addToCart.html',{'carts': cart})
#     else:
#         return HttpResponseRedirect('/profile/')

    

def application_internship(request):
    internship = Internship.objects.all()
    return render(request,'internships/internships.html',{'internship': internship} )


class ApplyInternship(View):
    def get(self, request, pk):
        interns = Internship.objects.get(pk=pk)
        return render(request, 'internships/applyinternship.html', {'i': interns})

def applyInternships(request):
    user = request.user
    intern_id = request.GET.get('intern_id')
    interns = Internship.objects.get(id=intern_id)
    intership_apply(user=user, internship=interns).save()
    return redirect('/profile')
    

def application_job(request):
    jobs = Job.objects.all()
    return render(request,'jobs/jobs.html',{'job':jobs})

class ApplyJobs(View):
    def get(self, request, pk):
        jobs = Job.objects.get(pk=pk)
        return render(request, 'jobs/applyjobs.html',{'j':jobs})

def jobsApplied(request):
    user = request.user
    jobs_id = request.GET.get('jobs_id')
    jobs = Job.objects.get(id=jobs_id)
    job_display(user=user, job=jobs).save()
    return redirect('/profile')



def feebbackmsg(request):
    if request.method == 'POST':
        formInfos = FeebbackForm(request.POST)
        if formInfos.is_valid():
            fn = formInfos.cleaned_data['first_name']
            ln = formInfos.cleaned_data['last_name']
            em = formInfos.cleaned_data['email_address']
            ph = formInfos.cleaned_data['phone']
            mg = formInfos.cleaned_data['message']
            reg = ContactUs(fname=fn, lname=ln,email=em, phone=ph, msg=mg)
            reg.save()

    else:
        formInfos = FeebbackForm()
    return render(request,'contact/contact.html',{'formval': formInfos})

def user_login(request):
    if not request.user.is_authenticated: 
        if request.method == "POST":
            form = logInform(request=request, data=request.POST)
            if form.is_valid():
                usrn = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=usrn, password=pwd)
                if user is not None:  
                    login(request, user)
                    messages.success(request, 'Logged In successfully')
                    return HttpResponseRedirect('/profile/')  

        else:
            form = logInform()
        return render(request, 'login/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')

def profileFunctions(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = userEditForm(request.POST, instance=request.user)
            user_img = UserProfileImage(request.POST ,instance=request.user.customer ,files=request.FILES)
            if fm.is_valid() and user_img.is_valid():
                fm.save()
                user_img.save()
                messages.success(request,'Your Profile is Updated')

        else:
            user = request.user
            buy_course = Cart.objects.filter(user=user)
            intlist = intership_apply.objects.filter(user=user)
            jobs = job_display.objects.filter(user=user)
            fm = userEditForm(instance=request.user)
            user_img = UserProfileImage(request.POST, instance=request.user.customer)
            
        return render(request, 'dashboad/dashboad.html', 
            {'name': request.user, 'form': fm,'course':buy_course,
            'user_img': user_img,'applied_intern':intlist,
            'job':jobs})
    else:
        return HttpResponseRedirect('/profile/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signUp(request):
    if request.method == "POST":
        form = singUpform(request.POST)
        if form.is_valid():
            messages.success(request, '✅ Signed Up successfully ✅')
            new_user = form.save(commit=False)
            new_user.save()
            Customer.objects.create(user=new_user)
            return HttpResponseRedirect('/singin/')

    else:
        form = singUpform()
    return render(request, 'signUp/signUp.html', {'form': form})
