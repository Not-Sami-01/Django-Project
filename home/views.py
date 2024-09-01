from django.shortcuts import render,HttpResponse
from home.models import Contact
from home.models import UserLogins
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def login(request):
    if request.method == 'POST':
        username = request.POST.get('myusername')
        if username is not None:
            username = username.lower()
        else:
            messages.warning(request,'Username Error')
        password = request.POST.get('mypassword')
        try:
            user = UserLogins.objects.get(username=username)
        except UserLogins.DoesNotExist:
            messages.warning(request,'Invalid username')
            return
        else:
            if check_password(password, user.password):
                request.session['username'] = username
                messages.success(request,'Logged in successfully')
            else:
                messages.warning(request,'Invalid password')
                return

    

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('signup_username')
        username = username.lower()
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')
        if(password == cpass):
            check_username_validity = UserLogins.objects.filter(username=username)
            if check_username_validity.exists():
                messages.warning(request,'Username is already taken')
                return
            else:
                encodedpass = make_password(password)
                newUser = UserLogins(username = username, password = encodedpass, datetime = datetime.today())
                newUser.save()
                messages.success(request,'Account created successful, Now you can login to our website')
        else: 
            messages.warning(request,'Passwords do not match')
            return

def sameThings(request):
    if request.method == 'POST':
        loginOrSignup = request.POST.get('login_or_signup')
        if loginOrSignup =='login':
            login(request)
        elif (request.POST.get('sigg') == 'signup'):
            signup(request)
    if request.method == 'GET':
        logout = request.GET.get('logout')
        if logout == 'true':
            del request.session['username']
            messages.warning(request,'Logged out successfully')

def index(request):
    sameThings(request)
    return render(request, 'index.html')

def about(request):
    sameThings(request)
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        if request.POST.get('email_or_phone') is not None:
            email_or_phone = request.POST.get('email_or_phone')
            firstName1 = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            context = request.POST.get('context')
            contact = Contact(firstName = firstName1, lastName = lastName, email_or_phone = email_or_phone, context = context, datetime = datetime.today())
            contact.save()
            messages.success(request, "Profile details updated.")

    sameThings(request)
    return render(request, 'contact.html')

def services(request):
    sameThings(request)
    return render(request, 'services.html')

# Create your views here. 