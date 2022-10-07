from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

# _____________________This Fuction will Add item and show all the item.______________________________
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm , email=em ,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})



# ________________________This function will Update____________________________________
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,id = pi)
        if fm.is_valid():
            id = fm.cleaned_data['id']
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(id =1,name=nm , email=em ,password=pw)
            fm.save()
           
    else:
        fm = StudentRegistration()
    return render(request,'enroll/updatestudent.html',{'formm':fm})


# ________________________This fuction will be Detele____________________________________________
def delete_data(request,id):
     if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

