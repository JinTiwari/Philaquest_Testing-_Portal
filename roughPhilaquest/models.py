from email.policy import default
from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#made this file on own and creating custom models

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Student_class = models.PositiveSmallIntegerField(null= True)
    No_Test_Taken =  models.PositiveSmallIntegerField(default = 0)
    Profilename = models.CharField(max_length = 25 ,default = "test")

    Test1 = models.BooleanField(default = False)
    Test2 = models.BooleanField(default = False)
    Test3 = models.BooleanField(default = False)
    Test4 = models.BooleanField(default = False)
    Test5 = models.BooleanField(default = False)
    Test6 = models.BooleanField(default = False)
    Test7 = models.BooleanField(default = False)

    response_test1 = models.CharField(max_length = 10000 , blank = True)
    response_test2 = models.CharField(max_length = 10000 , blank = True)
    response_test3 = models.CharField(max_length = 10000 , blank = True)
    response_test4 = models.CharField(max_length = 10000 , blank = True)
    response_test5 = models.CharField(max_length = 10000 , blank = True)
    response_test6 = models.CharField(max_length = 10000 , blank = True)
    response_test7 = models.CharField(max_length = 10000 , blank = True)

    def __str__(self) :
        return self.Profilename

    def update(self):
        n = 0
        if self.Test1 == True:
            n += 1
        if self.Test2 == True:
            n += 1
        if self.Test3 == True:
            n += 1
        if self.Test4 == True:
            n += 1
        if self.Test5 == True:
            n += 1
        if self.Test6 == True:
            n += 1
        if self.Test7 == True:
            n += 1
        
        self.No_Test_Taken = n

@receiver (post_save , sender = User)
def create_user_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver (post_save , sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class QuestionPaper (models.Model):
    Name = models.CharField(max_length = 20)
    DisplayName = models.CharField(max_length = 20 , default = "")
    Free = models.BooleanField(default = True)
    Date_created = models.DateField(null = True)

    def __str__(self) :
        return self.Name


class Questions (QuestionPaper):
    questNo = models.PositiveSmallIntegerField()
    ques_tion = models.CharField(max_length = 3000)
    option1 = models.CharField(max_length = 1000)
    option2 = models.CharField(max_length = 1000)
    option3 = models.CharField(max_length = 1000)
    option4 = models.CharField(max_length = 1000)
    Correc_option_choices = [
        ("Opt1" , "option1"),
        ("Opt2" , "option2"),
        ("Opt3" , "option3"),
        ("Opt4" , "option4")
    ]
    CorrectOption = models.TextField(choices = Correc_option_choices , null = False)

    Ques_image = models.ImageField(upload_to = "Question/img" , blank = True)
    def __str__(self) :
        return (str(self.questNo)+ " " +self.Name)

    



