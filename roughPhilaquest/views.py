from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Questions
from django.template.defaulttags import register
from .models import QuestionPaper

def loginPaage(request):
    return render(request,'index.html')

def signUp(request):
    return render(request , 'signup.html')

def confirmations(request):
    if request.method == "POST":
        # get the post parameters
        Username = request.POST['Username']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        email = request.POST['email']
        Sclass = request.POST['Class']
        Passowrd1 = request.POST['Passowrd1']
        Passowrd2 = request.POST['Passowrd2']

        #check for wrong inputs
        if len(Username) > 12:
            messages.error(request , "Please choose a smaller Username")
            return redirect ('signUp')
        if Passowrd1 != Passowrd2:
            messages.error(request , "Please Enter same passwords in both tthe fields!")
            return redirect ('signUp')
        if User.objects.filter(username = Username).first():
            messages.error(request, "This username is already taken")
            return redirect('signUp')

        #create User
        myuser = User.objects.create_user(Username,email , Passowrd1 , first_name = Fname , last_name = Lname )
        myuser.save()

        user = User.objects.filter(username = Username)[0]
        user.profile.Student_class = Sclass
        user.save()
        params = {"name" : Fname }
        return render(request , 'confirmations.html' , params)   

    else:
        return redirect('Welcome')

def loginformfill(request):
    return render(request , 'login.html')

def handleLogin(request):
    if request.method == 'POST':
        loginUsername = request.POST['username']
        loginPassword = request.POST['Passowrd']

        user = authenticate(username = loginUsername , password= loginPassword)

        if user is not None:
            login(request,user)
            # messages.success(request , "Successfully Logged In")
            return redirect("Udashboard")
        else:
            messages.error(request , "Please enter correct pair of credentials and try again!")
            return redirect('login')
    else:
        return redirect('login')
def handleLogout(request):
    logout (request)
    return redirect ('Welcome')

def dashboard(request):  
    ins = User.objects.get(username = request.user)
    params = {'username' : ins.first_name}
    return render(request , 'Udashboard.html' , params )

def testPage (request):
    # Getting test names available in backend!

    ins = QuestionPaper.objects.filter(Free = True)
    TestList = [ins[0].Name]
    TestList2 = [ins[0].DisplayName]
    n = 0
    for i in range(len(ins)):
        if TestList[n] != ins[i].Name :
            TestList.append(ins[i].Name)
            TestList2.append(ins[i].DisplayName)
            n += 1
    bothList = zip (TestList , TestList2)
    qns = User.objects.get(username = request.user)
    params = {"Compacted" : bothList , 'username' : qns.first_name}

    return render(request , 'test.html' , params)

def taketest (request):
    if request.method == "POST":
        name = str(request.POST.get("Test Name"))
        Quests = Questions.objects.filter(Name = name)
        n = len(Quests)
        qns = User.objects.get(username = request.user)
        params = {"Questions" : Quests , "range" : range(1,n) , "length" : n , "name" : name , 'username' : qns.first_name }
        return render(request , 'test.html' , params)
    else:
        return redirect("Udashboard")
        

def checkAnswers(request):
    if request.method == "POST":
        #get post parameters using for loop!
        name = request.POST.get("submitTestButton")
        Quests = Questions.objects.filter(Name = name)
        Answers = []
        
        for i in range(len(Quests)):
            Answers.append(request.POST.get(str(Quests[i].questNo)))

        # Checking for no input
        check = 0 
        for i in range (len(Quests)):
            if Answers[i] == None:
                check +=1
        if check >= (len(Quests))/2:
            messages.error(request , "Please attempt half of the test before submitting! ")
            return redirect ('TestPage')
        
        # checking number of correct answers!
        numCorrect = 0
        noAttempt = 0
        numIncorrect = 0
        n = len(Quests)
        for i in range (len(Quests)):
            if Answers [i] == Quests[i].CorrectOption :
                numCorrect += 1
            elif Answers [i] == None:
                noAttempt += 1
            else:
                numIncorrect += 1
        
        #updating the user model with answer key!
        Answers2 = []
        for i in range(len(Quests)):
            Answers2.append(Answers[i])
        AnswrString = ""
        for i in range (len (Quests)):
            temp = str(Answers2.pop())
            AnswrString +=  temp
            
        ins = User.objects.get(username = str(request.user))
        if name == "Paper1":
            ins.profile.Test1 = True
            ins.profile.response_test1 = AnswrString
        elif name == "Paper2":
            ins.profile.Test2 = True
            ins.profile.response_test2 = AnswrString
        elif name == "Paper3":
            ins.profile.Test3 = True
            ins.profile.response_test3 = AnswrString
        elif name == "Paper4":
            ins.profile.Test4 = True
            ins.profile.response_test4 = AnswrString
        elif name == "Paper5":
            ins.profile.Test5 = True
            ins.profile.response_test5 = AnswrString
        elif name == "Paper6":
            ins.profile.Test6 = True
            ins.profile.response_test6 = AnswrString
        elif name == "Paper7":
            ins.profile.Test7 = True
            ins.profile.response_test7 = AnswrString
        ins.save()
        ins.profile.update()
        ins.save()
        # print (ins)
        #passing the input and correct answer key in template for checking!
        SearchList = zip (Quests ,Answers )
        qns = User.objects.get(username = request.user)
        params = {"Compact":SearchList,"Questions" : Quests, "NumberOfCorrect" : numCorrect , "NumberOfIncorrect" : numIncorrect , "NotAnswered":noAttempt , "range" : range(1,n+1) , "1" : "Opt1" , "name" : name, 'username' : qns.first_name }
        
        return render (request , "test.html" , params)

    else :
        return redirect ('Udashboard')

@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg - 1]

def results(request):
    if request.method == "POST":
        #getting request 
        name = request.POST.get("TestName")
        #   Getting users response to the corresponding test
        ins = User.objects.get(username = str(request.user))
        Answerkey = []
        if name == "Paper1":
            Answerkey = list(ins.profile.response_test1)
        elif name == "Paper2":
            Answerkey = list(ins.profile.response_test2)
        elif name == "Paper3":
            Answerkey = list(ins.profile.response_test3)
        elif name == "Paper4":
            Answerkey = list(ins.profile.response_test4)
        elif name == "Paper5":
            Answerkey = list(ins.profile.response_test5)
        elif name == "Paper6":
            Answerkey = list(ins.profile.response_test6)
        elif name == "Paper7":
            Answerkey = list(ins.profile.response_test7)
        
        n = int(len(Answerkey) / 4)
        Answerkey = Answerkey[::-1]
        Answers = []
        for i in range(n):
            temp4 = Answerkey.pop()
            temp3 = Answerkey.pop()
            temp2 = Answerkey.pop()
            temp1 = Answerkey.pop()
            Answers.append(temp4+temp3+temp2+temp1)
        Answers = Answers[::-1]
        # Getting answer key of the corresponding test
        Quests = Questions.objects.filter(Name = name)
        
        numCorrect = 0
        noAttempt = 0
        numIncorrect = 0
        for i in range (len(Quests)):
            if Answers [i] == Quests[i].CorrectOption :
                numCorrect += 1
            elif Answers [i] == "None":
                noAttempt += 1
            else:
                numIncorrect += 1

        #zipping list and request
        SearchList = zip (Quests ,Answers )
        qns = User.objects.get(username = request.user)
        #passing the dictionary in render
        params = {"Compact":SearchList, "NumberOfCorrect" : numCorrect , "NumberOfIncorrect" : numIncorrect , "NotAnswered":noAttempt,  'username' : qns.first_name , "name" : Quests[0].DisplayName }

        return render(request , "results.html" , params)

    else:
        qns = User.objects.get(username = request.user)
        ins = QuestionPaper.objects.filter(Free = True)
        TestList = [ins[0].Name]
        TestList2 = [ins[0].DisplayName]
        n = 0
        for i in range(len(ins)):
            if TestList[n] != ins[i].Name :
                TestList.append(ins[i].Name)
                TestList2.append(ins[i].DisplayName)
                n += 1
        print (TestList)
        params = {'username' : qns.first_name , "instance" : qns.profile , "TestTaken" : str(qns.profile.No_Test_Taken) , "TestList" : TestList , "TestList2" : TestList2}
        return render(request , "results.html" ,params )