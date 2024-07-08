from calendar import c
import email
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from. models import student_Details
# from.models import Edit_Profile

# Create your views here.
def home(request):
    # return HttpResponse('this is student page')
    return render(request,'student/html/login.html')

def student_login(request):
    # if request.method == 'POST':
        user_id=request.POST["txtid"]
        user_password=request.POST["txtpassword"]
        print(user_id,user_password)
        custom_user=authenticate(request,username=user_id,password=user_password)

        if custom_user is not None:
            login(request,custom_user)
            return render(request,"student/html/student_home.html")

        else:
            messages.error(request,"Invalid credentials")
        return redirect("home")

def student_details(request):
    if request.method == 'GET':

        student_query_set=student_Details.objects.filter(student_id=request.user.id)
        print(len(student_query_set))
        if len (student_query_set)>0:
            messages.info(request,"you have already added the details")
            return render(request,"student/html/student_home.html")##student editdetail

        return render(request,'student/html/student_details.html')

    if request.method == 'POST':
        city=request.POST["city"]
        phone=request.POST["txtphone"]
        address=request.POST["txtaddress"]

        sd=student_Details(student_id=request.user.id,phone=phone,city=city,address=address)
        sd.save()
        messages.success(request,"details has been saved")
        print("deatils saved")
    return redirect("home")
    
def edit_profile(request):
    if request.method == 'GET':
        return render(request,'student/html/edit_profile.html')

    if request.method == 'POST':
        em=request.POST["txtemail"]
        first_nm=request.POST["txtfirstname"]
        last_nm=request.POST["txtlastname"]

        s_id=request.user.id #logged in student (user) id
        print("loggedin student id is",s_id)
        student_user_object=User.objects.get(id=s_id)#will fetch a single object
        student_user_object.email=em
        student_user_object.first_name=first_nm
        student_user_object.last_name=last_nm
        student_user_object.save()
        context={"user":student_user_object}
        print("profile edited successfully")
        messages.success(request,"profile updated successfully",)

    return render(request,'student/html/edit_profile.html',context)

def student_logout(request):
    logout(request)
    messages.success(request,"successfully logout")
    return redirect("home")
  
