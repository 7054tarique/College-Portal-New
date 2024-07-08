from django.contrib import admin
from .models import  Notice, Course_Detail, Contact, Job,AdministrativeStaff,Consultancy

class Course_DetailAdmin(admin.ModelAdmin):
    list_display=('course_name','fees','duration','description')# it will show data in tabular formatt

class Consultancy_Admin(admin.ModelAdmin):
    list_display=('name','email','phone','city')#tuple
    list_filter=['city']#list
    search_fields=('name','city')






# Register your models here.
admin.site.register(Notice)

admin.site.register(Course_Detail,Course_DetailAdmin)

admin.site.register(Contact)

admin.site.register(Job)

admin.site.register(AdministrativeStaff)

admin.site.register(Consultancy,Consultancy_Admin)


##########customise admin pannel Text#############

admin.site.site_header="College Portal Administrations"
admin.site.site_title="College Portal Admin Dashboard"
admin.site.index_title="Welcome to CollegePortal"