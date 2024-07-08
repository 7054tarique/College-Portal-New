from django.urls import path
from . import views
urlpatterns= [
    path("",views.home,name="home"),
    path("student_login/",views.student_login,name="student_login"),
    path("student_details/",views.student_details,name="student_details"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("student_logout/",views.student_logout,name="student_logout"),


    
]