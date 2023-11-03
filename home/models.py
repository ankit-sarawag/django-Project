from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=10)
    desc = models.TextField(max_length=100)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.name + " " + self.email


class CourseMentorMapping(models.Model):
    course = models.CharField(max_length=70, unique=True)
    mentor = models.CharField(max_length=80)

    def __str__(self):
        return self.course
    

class RegisterStudent(models.Model):
    genderBoolChoice = (
        ("M","Male"),("F","Female")
    )
    streamBoolChoice = (
        ("Sci","Science"),("Com","Commerce"),("Arts","Arts")
    )
    sectionBoolChoice = (
        ("A","A"),("B","B"),("C","C"),("D","D"),
    )

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    phone = models.IntegerField()
    primaryEmail = models.EmailField()
    alternateEmail = models.EmailField()
    password = models.CharField(max_length=10)
    rollno = models.IntegerField()
    birthDate = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=1,choices=genderBoolChoice)
    stream = models.CharField(max_length=4,choices=streamBoolChoice)
    course = models.CharField(max_length=70,null=True)
    mentor = models.CharField(max_length=80, blank=True, null=True)
    semester = models.IntegerField()
    section = models.CharField(max_length=1,default="A",choices=sectionBoolChoice,null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.username + " " + self.primaryEmail 
    
    def save(self, *args, **kwargs):
        if self.course:
            try:
                course_mapping = CourseMentorMapping.objects.get(course=self.course)
                self.mentor = course_mapping.mentor
            except CourseMentorMapping.DoesNotExist:
                self.mentor = "Default Mentor"  # Default mentor when there is no mapping
        super(RegisterStudent, self).save(*args, **kwargs)

    def __str__(self):
        return self.username + " " + self.primaryEmail
 
 



