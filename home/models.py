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


# class CourseMentorMapping(models.Model):
#     course = models.CharField(max_length=70, unique=True)
#     mentor = models.CharField(max_length=80)
#     student = models.ForeignKey('RegisterStudent', on_delete=models.CASCADE, related_name='courses', null=True, blank=True)
#     def __str__(self):
#         return self.course
# mapping1 = CourseMentorMapping(course="Bcom(h)", mentor="Dr.")
# mapping2 = CourseMentorMapping(course="CS(h)", mentor="Dr. VS Dixit")
# mapping1.save()
# mapping2.save()
# # Create the mappings for courses and their corresponding conveyors
# mapping1 = CourseMentorMapping(course="Bcom(h)", mentor="Dr.")
# mapping2 = CourseMentorMapping(course="CS(h)", mentor="Dr. VS Dixit ")

# # Save the mappings to the database
# mapping1.save()
# mapping2.save()

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

    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=50)
    phone = models.IntegerField()
    primaryEmail = models.EmailField()
    alternateEmail = models.EmailField()
    password = models.CharField(max_length=10)
    rollno = models.IntegerField()
    birthDate = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=1,choices=genderBoolChoice)
    stream = models.CharField(max_length=4,choices=streamBoolChoice)
    course = models.CharField(max_length=70)
    # mentor = models.CharField(max_length=80, blank=True,null=True)
    semester = models.IntegerField()
    section = models.CharField(max_length=1,default="A",choices=sectionBoolChoice,null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.username + " " + self.primaryEmail 
    # @property
    # def mentor(self):
    #     # Retrieve the mentor value based on the selected course
    #     mapping = self.courses.first()  # Get the first associated course
    #     if mapping:
    #         return mapping.mentor
    #     return ""

    # @mentor.setter
    # def mentor(self, value):
    #     # This setter allows you to set the mentor field if needed
    #     self._mentor = value
 

