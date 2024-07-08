from django.urls import path
from.import views,consultancy_views
urlpatterns=[
    path("",views.home,name="home"),
    path("aboutus/",views.aboutus,name="aboutsus"),
    path("contactus/",views.contactus,name="contactus"),
    path("feedback/",views.feedback,name="feedback"),
    # path("login/",views.login,name="login"),
    path("Job/",views.job,name="job"),
    path("course/",views.Course,name="course"),
    path("registration/",consultancy_views.registration,name="registration"),
    path("login/",consultancy_views.login,name="login"),
    path("edit_profile/",consultancy_views.Edit_Profile.as_view(),name="edit_profile"),
    path("logout/",consultancy_views.sign_out,name="logout"),
    path("enquiry/",views.enquiry,name="enquiry"),
    path("validate_consultancy_username/",consultancy_views.validate_consultancy_username,name="validate_consultancy_username"),
    path("view_contents/<int:id>",views.view_contents,name="view_contents"),
]