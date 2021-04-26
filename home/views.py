from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from appointments.models import Doctor, Patient
import bcrypt
from django.contrib.auth.models import User
from tkinter import *
from django.contrib.auth.hashers import make_password

from home.models import Account
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

        if(request.POST.get("user")=="patient"):
            if (User.objects.filter(username=request.POST['username']).exists()):
                
                user = User.objects.get(username=request.POST['username'])
              
                temp_pass = request.POST['password']
            
                if (user.check_password(temp_pass)):
                    print("correct password")
                    if(Patient.objects.filter(user=user).exists()):
                        request.session['id'] = user.id
                        request.session['user_type'] = "0"
                        return redirect("/")
                        # return render(request, 'HomePage.html', {'user_type': "0"})
                
                print("Incorrect username or password")
                form = Login() 
                return render(request, 'login.html', {'form':form, 'error':"Incorrect Username or Password"})
            else:
                form = Login() 
                return render(request, 'login.html', {'form':form, 'error':"Username Doesn't Exist"})
        elif(request.POST.get("user")=="doctor"):
            if (User.objects.filter(username=request.POST['username']).exists()):   
                user = User.objects.get(username=request.POST['username'])
              
                temp_pass = request.POST['password']
            
                if (user.check_password(temp_pass)):
                    print("correct password")
                    if(Doctor.objects.filter(user=user).exists()):
                        request.session['id'] = user.id
                        request.session['user_type'] = "1"
                        return redirect("/")
                        # return render(request, 'HomePage.html', {'user_type': "1"})
                
                print("Incorrect username or password")
                form = Login() 
                return render(request, 'login.html', {'form':form, 'error':"Incorrect Username or Password"})
            else:
                form = Login() 
                return render(request, 'login.html', {'form':form, 'error':"Username Doesn't Exist"})

    else:
        form = Login()    
    return render(request, 'login.html', {'form':form})






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
            password = userform['password']

            

            if(request.POST.get("user")=='patient'):

                if User.objects.filter(username=request.POST['username']).exists():
                    print("Username unavailable")
                    return render(request, 'register.html', {'form': form, 'error': "Username already exists"})

                if User.objects.filter(email=request.POST['email']).exists():
                    print("Email unavailable")

                    return render(request, 'register.html', {'form': form, 'error1': "Email already exists"})

                print(password)
                #if not (Patient.objects.filter(user=request.POST['username']).exists() and Patient.objects.filter(email=request.POST['email']).exists()):
                user = User.objects.create(username=username, email=email, password=make_password(password))
                print("User password: " , user)
                Patient.objects.create(user=user)
                request.session['id'] = user.id
                request.session['user_type'] = "0"
                return redirect("../account/")

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
                request.session['id'] = user.id
                request.session['user_type'] = "1"
                return redirect("../account/")

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
        S = User.objects.all()

    #print("type of S:",type(S))
    return render(request, 'register.html', {'form': form,'S':S})





def HomePage(request):
    # print(request.session['id']) #ONLY WHEN LOGGEDIN OR SIGNEDUP
    if(request.session['id'] != None):
        isloggedIn = 1
        if (request.session['user_type'] == "0"):
            usertype = 0
        else:
            usertype = 1
    else:
        isloggedIn = 0
        usertype = None



    return render(request, 'HomePage.html', {'isloggedIn': isloggedIn , 'usertype': usertype})





def logout(request):
    request.session['id'] = None
    return redirect("/")
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