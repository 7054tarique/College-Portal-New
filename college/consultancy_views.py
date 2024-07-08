from django.shortcuts import render,HttpResponse,redirect
from .models import Consultancy
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout
from django.http import JsonResponse

def registration(request):
    if request.method=="GET":
      return render(request,'college/html/registration.html')
    if request.method=="POST":
        user_id=request.POST["txtusername"]
        user_password=request.POST["txtpassword"]
        user_name=request.POST["txtname"]
        user_email=request.POST["txtemail"]
        user_phone=request.POST["txtphone"]
        user_city=request.POST["city"]
        user_address=request.POST["txtaddress"]

        consultancy=Consultancy.objects.filter(user_id=user_id)
        if len(consultancy)>0:
            messages.error(request,"this is already exist")
            return redirect("registration")
        else:

         consultancy_object=Consultancy(user_id=user_id,paasword=user_password,name=user_name,email=user_email,phone=user_phone,city=user_city,address=user_address)
        consultancy_object.save()
        print("consultancy registration done")
        messages.success(request,"Registration done successfully,Please Do Login")
        return render(request,'college/html/registration.html')

def login(request):
    if request.method=="GET":
       return render(request,'college/html/login.html')
    if request.method=="POST":
        user_name=request.POST["txtusername"]
        user_password=request.POST["txtpassword"]
        consultancy_query_set=Consultancy.objects.filter(user_id=user_name,paasword=user_password)
        print(len(consultancy_query_set))
        if len(consultancy_query_set)>0:

            request.session["session_key"]=user_name #storing values in session
            #request.session["abc"]=xyz
            context={"consultancy_key":consultancy_query_set}
            
            return render(request,'college/html/consultancy/consultancy_home.html',context)
        else:
            messages.success(request,"Invalid UserId or Password")
            return redirect("login")
class Edit_Profile(View):
    def get(self, request):

        id=request.session["session_key"] #getting value from session
        consultancy_obj=Consultancy.objects.get(user_id=id)
        context={
            "obj_key":consultancy_obj #binding objects with key and store in to dict

        }
        return render(request,'college/html/consultancy/edit_profile.html',context)

    def post(self, request):
        id=request.session["session_key"] #getting value from session
        email=request.POST["txtemail"]
        phone=request.POST["txtphone"]
        address=request.POST["txtaddress"]
        consultancy_obj=Consultancy.objects.get(user_id=id)
        consultancy_obj.email=email
        consultancy_obj.phone=phone
        consultancy_obj.address=address
        consultancy_obj.save()
        print("profile updated successfully")
        messages.success(request,"profile updated successfully",)
        consultancy_obj=Consultancy.objects.get(user_id=id)# after saving data we are fetchong new value
        context={
            "obj_key":consultancy_obj #binding objects with key and store in to dict

        }
        return render(request,'college/html/consultancy/edit_profile.html',context)

def sign_out(request):
     
     del request.session["session_key"]# destroying the session
     logout(request)
     return redirect("login")


def validate_consultancy_username(request):
    username=request.GET['username']
    data={
        'exists':Consultancy.objects.filter(user_id__iexact=username).exists()
        }
    return JsonResponse(data)  




