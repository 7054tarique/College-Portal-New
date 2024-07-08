from django.shortcuts import render,HttpResponse,redirect
from .models import Course_Detail, Notice,Job,Contact, User_Feedback,Consultancy,AdministrativeStaff
from django.contrib import messages
from .forms import EnquiryForm
# Create your views here.
def home(request):
    # return HttpResponse("this is home page")
    notice_query_set=Notice.objects.all()#it will access all the records from table
    #it will return queryset 
    
    print(notice_query_set)
    admin_staff=AdministrativeStaff.objects.all()
    context={
        "notice_key":notice_query_set,
        "staff_key":admin_staff

    }
   
    return render(request,'college/html/index.html',context)#passing the dict html page
def aboutus(request):
    return render(request,'college/html/aboutus.html')
def contactus(request):
    if request.method=="GET":
       return render(request,'college/html/contactus.html')
    if request.method=="POST":
        
        nm=request.POST["txtname"]#request.POST is a dict control name is key for dict
        em=request.POST["txtemail"]
        ph=request.POST["txtphone"]
        query=request.POST["txtquery"]
        print(nm,em,ph,query)
        contactobj=Contact(name=nm,email=em,phone=ph,your_query=query)# creating Contact class object
        contactobj.save()#we are saving data in to contact table
        print("data has been saved")
        messages.success(request,"Thank for contacting us we will reply soon")

        return render(request,'college/html/contactus.html')
def feedback(request):

    if request.method=="GET":
        return render(request,'college/html/feedback.html')
    if request.method=="POST":
        nm=request.POST["txtname"]
        rt=request.POST["txtratings"]
        re=request.POST["txtreview_text"]

        print(nm,rt,re)
        feedbackobj=User_Feedback(name=nm,ratings=rt,review_text=re)
        feedbackobj.save()
        print("data has been saved")
        messages.success(request,"Thank you to give me your feedback")

        

    return render(request,'college/html/feedback.html')


def job(request):
    job_query_set=Job.objects.all()
    print(job_query_set)
    job_dict={
        "job_key":job_query_set
    }
    return render(request,'college/html/job.html',job_dict)
def Course(request):
    course_query_set=Course_Detail.objects.all()
    print(course_query_set)
    course_dict={
        "course_key":course_query_set
    }
    return render(request,'college/html/course.html',course_dict)


    ##################### to show controls enquiry.html##################
def enquiry(request):

    if request.method =='GET':
        form_obj=EnquiryForm()
        context={"form_key":form_obj}
        return render(request,'college/html/enquiry.html',context)
    
    if request.method =='POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            print("query has been saved succesfully")

            return redirect('enquiry')

def view_contents(request,id):
    notice_obj=Notice.objects.get(notice_id=id)
    context={"notice_key":notice_obj}
    return render(request,'college/html/view_notice_content.html',context)

