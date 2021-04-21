from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from appointments.models import Doctor, Patient
import bcrypt
from django.contrib.auth.models import User
from tkinter import *


# Create your views here.

#region Helper functions
from hashlib import sha256

# def getJWToken():
#     redirect('token_obtain_pair')
def hashPassword(plain):
    print(plain)
    return bcrypt.hashpw(plain.encode('utf8'), bcrypt.gensalt())
    #return sha256(plain.rstrip().encode()).hexdigest()
#endregion


def index(request):
    # return render(request,'index.html')
    return render(request, 'HomePage.html')

def login(request):
    if request.method == 'POST':

        if (User.objects.filter(username=request.POST['username']).exists()):
            user = User.objects.filter(username=request.POST['username'])[0]
            user_pass = ""
            for i in range(2, len(user.password)-1):
                user_pass += user.password[i]
            
            temp_pass = request.POST['password']

            if (bcrypt.checkpw(temp_pass.encode('utf8'), user_pass.encode('utf8'))):
                print("correct password")
                request.session['id'] = user.user_id

            else:
                print("Incorrect username or password")
                form = Login() 
                return render(request, 'login.html', {'form':form, 'error':"Incorrect Username or Password"})

        #request.session.user_id = 1

        return redirect("../HomePage")
    else:
        form = Login()    
    return render(request, 'login.html', {'form':form})


def HomePage(request):
    # print(request.session['id']) #ONLY WHEN LOGGEDIN OR SIGNEDUP
    return render(request, 'HomePage.html')

def register(request):
    
    if request.method == 'POST':
        #print("register post")

        form = Register(request.POST)

        if form.is_valid():

            userform = form.cleaned_data
            print("FORM", userform)
            #userid = userform['user_id'] #autogenerated
            username = userform['username']
            email = userform['email']
            password = hashPassword(userform['password'])


            if(request.POST.get("user")=='patient'):

                if User.objects.filter(username=request.POST['username']).exists():
                    print("Username unavailable")
                    return render(request, 'register.html', {'form': form, 'error': "Username already exists"})

                if User.objects.filter(email=request.POST['email']).exists():
                    print("Email unavailable")
                    return render(request, 'register.html', {'form': form, 'error1': "Email already exists"})

                #if not (Patient.objects.filter(user=request.POST['username']).exists() and Patient.objects.filter(email=request.POST['email']).exists()):
                user = User.objects.create_user(username=username, email=email, password=password)
                Patient.objects.create(user=user)
                print("userID: ", user.id)
                return redirect("../account/"+str(user.id)+"/0")

            if (request.POST.get("user") == 'doctor'):

                if User.objects.filter(username=request.POST['username']).exists():
                    print("Username unavailable")
                    return render(request, 'register.html', {'form': form, 'error': "Username already exists"})

                if User.objects.filter(email=request.POST['email']).exists():
                    print("Email unavailable")
                    return render(request, 'register.html', {'form': form, 'error1': "Email already exists"})

                #if not (Doctor.objects.filter(user=request.POST['username']).exists() and Doctor.objects.filter(email=request.POST['email']).exists()):
                user = User.objects.create_user(username=username, email=email, password=password)
                Doctor.objects.create(user=user)
                return redirect("../account/" + str(user.id) + "/1")

            #Render on page (Not needed for API)
            S=Account.objects.all()
            # print("type of S:",type(S))
            # getJWToken()
            #Not run:
            # return render(request, 'register.html', {'form': form,'S':S})
            #print("redirecting now")

    else:
        #print("register get")
        form = Register()
        S = Account.objects.all()

    #print("type of S:",type(S))
    return render(request, 'register.html', {'form': form,'S':S})

'''
def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)
'''