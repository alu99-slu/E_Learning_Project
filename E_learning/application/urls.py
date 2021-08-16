from django.urls import path
from django.urls.conf import include
from . import views
from .authinticationform import password_resetForm, passwod_confirm_form, changePassword,logInform
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.application_home),
    path('about/', views.application_about),
    path('course/', views.CourseView.as_view()),
    #path('course/<slug:data>',views.filterCourse, name="courseData"),
    path('buy-course/<int:pk>', views.BuyCourse.as_view(), name='buy-course'),
    path('buy-courses/', views.buyCourses),
    path('add-to-cart/', views.addtocart),
    path('cart/',views.cartCourses),
    #path('course/',views.filterCourse, name="filterMob"),
    path('internships/', views.application_internship),
    path('apply-internships/<int:pk>', views.ApplyInternship.as_view(), name='apply-internships'),
    path('internship_applied/', views.applyInternships),
    path('jobs/', views.application_job),
    path('apply-jobs/<int:pk>',views.ApplyJobs.as_view(), name='apply-jobs'),
    path('jobsApplied/', views.jobsApplied),
    path('contact/', views.feebbackmsg),
    path('profile/', views.profileFunctions),
    path('singin/', views.user_signUp),
    path('login/', views.user_login,name='login'),
    path('social-auth/',include('social_django.urls',namespace='social')),

    # change password
    path('change-password/', auth_view.PasswordChangeView.as_view(
        template_name='login/changePwd.html', form_class=changePassword, success_url='/password-change-done/'), name='change-password'),
    # change password conformation
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(
        template_name='login/passwordchangedone.html'),
        name='password-change-done'),

    path('password_reset/', auth_view.PasswordResetView.
         as_view(template_name='login/password_reset.html',
                 form_class=password_resetForm),
         name='password_reset'),

    path('password_reset/done/', auth_view.PasswordResetDoneView.
         as_view(template_name='login/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.
         as_view(template_name='login/password_reset_confirm.html',
                 form_class=passwod_confirm_form),
         name='password_reset_confirm'),

    path('password_reset_complete/',auth_view.PasswordResetCompleteView.
         as_view(template_name="login/password_reset_complete.html"), name='password_reset_complete'),

    path('logout/', views.user_logout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
