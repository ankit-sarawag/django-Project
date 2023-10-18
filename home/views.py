from django.shortcuts import render,HttpResponse,redirect
from home.models  import Contact,RegisterStudent
from datetime import datetime
from django.contrib import messages

from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import logout,authenticate,login

from django.contrib.sessions.models import Session


# password for test user is ankit123456789$
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'home.html')
    
    # return HttpResponse("THis is the home page")
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'about.html')
    # return HttpResponse("THis is the about us page")

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        print("data fetched")
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        desc = request.POST.get('desc')
        date = datetime.today()
        print(name,phone,email,password,desc)
        ins = Contact(name=name,phone=phone,email=email,password=password,desc=desc,date=date)
        ins.save()
        messages.success(request,"Welcome to the amazing world of ARSD College!")
        print("data has been written")
    return render(request,'contact.html',{"name":request.POST.get('name')})
    # return HttpResponse("THis is the contact page")

def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'services.html')
def career(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'career.html')
    # return HttpResponse("THis is the career page")
def downloads(request):
    return render(request,'downloads.html')
    # return HttpResponse("THis is the achievements page")
def research(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'research.html')
    # return HttpResponse("THis is the achievements page")


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.warning(request,"You don't have an account in our database. Please register yourself and then login again")
            return render(request,"login.html",{"name":username})
        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('repeatpassword')
        user = User.objects.create_user(username=username,email=email,password=password)
        print("entry has been added")
        messages.success(request,"Congratulations your entry has been added in the database")
    
    return render(request,'signup.html',{"name":request.POST.get('username')})

def register(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context = {
            "name":request.POST.get('firstname'),
            "success":False
        }
    if request.method == "POST":
        print("data fetched")
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lname')
        username = firstname + " " + lastname
        phone = request.POST.get('phone')
        primaryEmail = request.POST.get('pemail')
        alternateEmail = request.POST.get('aemail')
        rollnumber = request.POST.get('rollno')
        password = request.POST.get('cpassword')
        birthdate = request.POST.get('birthDate')
        gender = request.POST.get('gender')
        stream = request.POST.get('stream')
        course = request.POST.get('course')
        semester = request.POST.get('semester')
        section = request.POST.get('section')
        date = datetime.today()
        print(firstname,phone,primaryEmail,password)
        ins = RegisterStudent(firstname=firstname,lastname=lastname,username=username,phone=phone,primaryEmail=primaryEmail,alternateEmail=alternateEmail,rollno=rollnumber,password=password,birthDate=birthdate,gender=gender,stream=stream,course=course,semester=semester,section=section,date=date)
        
        
        if(request.POST.get('key') == '1234' and len(rollnumber)==5 and len(phone) == 10):
            ins.save()
            messages.success(request,"Congratulations the student has been added in the database")
            print("data has been written")
            context={"success": True}
            
        else:
            if(request.POST.get('key') !='1234'):
                messages.warning(request,"you don't have the registration key to add data")
            elif(len(rollnumber) !=5):
                messages.warning(request,"The length of roll number should be equal to 5")
            elif(len(phone) != 10):
                messages.warning(request,"The length of phone number should be equal to 10")         
    return render(request,'register.html',context)

def loginStudent(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        username = request.POST.get('username')
        rollnumber = request.POST.get('rollno')
        password = request.POST.get('password')
        print(username,rollnumber,password)
        
        check_if_user_exists = RegisterStudent.objects.filter(rollno=rollnumber,username=username,password=password).exists()
        
        if check_if_user_exists:
                request.session["student_logged_in"] = True
                request.session["student_rollnumber"] = rollnumber
                return redirect("StudentDetails")
        else:
            messages.warning(request,"You don't have an account in our database. Please register yourself and then login again")
            return render(request,"loginStudent.html",{"name":username})
    
    # student = RegisterStudent.objects.all()
    return render(request,'loginStudent.html')

def logoutStudent(request):
    # rollnumber = request.session.get("student_rollnumber")

    # Check if the student session exists
    # if Session.objects.filter(session_key=request.session.session_key, session_data=rollnumber).exists():
    # #     Delete the student's session
    #     Session.objects.filter(session_key=request.session.session_key,).delete()
        
    # #     Clear the session data for the current request
    #     request.session.flush()
    if request.session.get("student_logged_in"):
        # Clear the student-specific session variables
        del request.session["student_logged_in"]
        del request.session["student_rollnumber"]
    return redirect("loginStudent")
    


def StudentDetails(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if not request.session.get("student_logged_in"):
        return redirect("/loginStudent")
    
    
    rollnumber = request.session.get("student_rollnumber")

    # Use the rollnumber to filter the database
    studentDetails = RegisterStudent.objects.get(rollno=rollnumber)
    
    return render(request,'StudentDetails.html',{"studentDetails": studentDetails})

def updateDetails(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if not request.session.get("student_logged_in"):
        return redirect("/loginStudent")
    
    rollnumber = request.session.get("student_rollnumber")

    
    studentDetails = RegisterStudent.objects.get(rollno=rollnumber)
    context = {
            "name":request.POST.get('firstname'),
            "success":False
    }
    if request.method == "POST":
        print("data fetched")
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lname')
        username = firstname + " " + lastname
        phone = request.POST.get('phone')
        alternateEmail = request.POST.get('aemail')
        password = request.POST.get('cpassword')
        date = datetime.today()
        print(firstname,phone,password)
        studentDetails.firstname=firstname
        studentDetails.lasttname=lastname
        studentDetails.usernamename=username
        studentDetails.phone=phone
        studentDetails.alternateEmail=alternateEmail
        studentDetails.password=password
        studentDetails.date=date
        
        
        if( len(rollnumber)==5 and len(phone) == 10):
            studentDetails.save()
            messages.success(request,"Congratulations! your details has updated in the database")
            print("data has been written")
            context={"success": True}
            
        else:
            
            if(len(rollnumber) !=5):
                messages.warning(request,"The length of roll number should be equal to 5")
            elif(len(phone) != 10):
                messages.warning(request,"The length of phone number should be equal to 10")  
    # Use the rollnumber to filter the database
    # studentDetails = RegisterStudent.objects.get(rollno=rollnumber)
    return render(request,'updateDetails.html',context)