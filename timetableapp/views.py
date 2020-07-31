from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import data

# Create your views here.
def index(request):
    # if user is registered display timetable creation page else
    # display index page
    if request.user.is_authenticated:
        return render(request,"timetableapp/homepage.html")
    else:
        return render(request,"timetableapp/index.html")

# user registration
def registerpage(request):
    return render(request,"timetableapp/registerpage.html")

def loginpage(request):
    return render(request,"timetableapp/loginpage.html")

def handleregister(request):
    if request.method=="POST":
        emailid=request.POST['emailid']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password!=cpassword:
            messages.add_message(request, messages.ERROR, 'Both Password doesnt match')
            return redirect('/registerpage')
        try:
            user = User.objects.create_user(emailid, emailid, password)
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Account already Created, Please Login')
            return redirect('/registerpage')
        createrecord=data(content='Please Delete this line and create a Time Table',user=user)
        createrecord.save()
        messages.add_message(request, messages.SUCCESS, 'Account Created Successfully')
    else:
        return HttpResponse("404 - Not Found")
    return render(request,"timetableapp/loginpage.html")

def handlelogin(request):
    if request.method=='POST':
        emailid=request.POST['emailid']
        password=request.POST['password']
        print(emailid, password)
        user=authenticate(username=emailid,password=password) #validating user
        print(user)
        if user is not None: #returns None if not found.
            login(request,user)
            messages.add_message(request,messages.SUCCESS,f"Welcome {user.username}")
            return redirect('/homepage')
        else:
            messages.error(request, "Invalid Credentials. Please Try Again!")
            return redirect('/loginpage')
    else:
        return HttpResponse("404 - Not Found")

def handlelogout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Successfully Logged Out')
    return redirect('/')

# timetable creation and updation page
def homepage(request):
    if request.user.is_authenticated:
        user=request.user
        if data.objects.filter(user=user):
            savedcontent=data.objects.filter(user=user)
            # print(savedcontent)
            # print(type(savedcontent))
            return render(request,"timetableapp/homepage.html",{'savedcontent':savedcontent})
        else:
            return render(request,"timetableapp/homepage.html")
    else:
        return render(request,"timetableapp/index.html")

#for saving content
def handledata(request):
    if request.method=="POST":
        table_id=request.POST.get('table_id')
        content=request.POST.get('content')
        user=request.user
        print("Details fetched:- ",table_id,content,user)
        fetchdata = data.objects.get(table_id=table_id)
        fetchdata.content=content
        fetchdata.save()
        messages.add_message(request,messages.SUCCESS,'Saved Successfully')
        return redirect('/homepage')
    else:
        return HttpResponse("404 - Not Found")
    