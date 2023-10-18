from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("career",views.career,name='career'),
    path("services",views.services,name='services'),
    path("downloads",views.downloads,name='downloads'),
    path("research",views.research,name='research'),
    
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
    path("signup",views.signup,name='signup'),
    path("register",views.register,name='register'),
    path("loginStudent",views.loginStudent,name='loginStudent'),
    path("StudentDetails",views.StudentDetails,name='StudentDetails'),
    path("logoutStudent",views.logoutStudent,name='logoutStudent'),
    path("updateDetails",views.updateDetails,name='updateDetails'),
    
    
    
    
]