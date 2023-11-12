from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
from .models import chatInfo,addlist
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import logout

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        login_url = reverse('userApp:login')
        return redirect(login_url)
    ## Addlist and search User ID
    if request.method == "POST":
        search = request.POST['search']
        if addlist.objects.filter(username = request.user.username,addedUserName = search).exists():
            messages.error(request,"User alredy exist")
        else:
            if User.objects.filter(username = search).exists():
                add = addlist(username = request.user.username,addedUserName = search)
                messages.error(request,"UserID Added")
                add.save()
            else:
                messages.error(request,"User not found")
    addList = addlist.objects.filter(username = request.user.username)
    return render(request,"home.html",{'addList':addList})
## Login
def login(request):
    if request.user.is_authenticated:
        home_url = reverse('userApp:home')
        return redirect(home_url)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('userApp:home')
        else:
            print("Incorect password or username")
    return render(request,"login.html")
## Signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        co_password = request.POST['co_password']
        if password == co_password:
            if User.objects.filter(username = username):
                return redirect('userApp:signup')
            elif User.objects.filter(email = email):
                return redirect('userApp:signup')
            else:
                info = User.objects.create_user(username = username,email = email,password = password)
                info.save()
                return redirect('userApp:login')
    return render(request,"signup.html")

def chat(request,username):
    if not request.user.is_authenticated:
        login_url = reverse('userApp:login')
        return redirect(login_url)
    if request.method == "POST":
        message = request.POST['message']
        mesAdd = chatInfo(userName = request.user.username,senderName = username,userMessage = message)
        mesAdd.save()
    addList = addlist.objects.filter(username = request.user.username)
    return render(request,"chat.html",{'senderName':username,'addList':addList})
def getData(request,username):
    user_messages = chatInfo.objects.filter(Q(userName=request.user.username, senderName=username) | Q(userName=username, senderName=request.user.username))
    return JsonResponse({"messages":list(user_messages.values())})

def Logout(request):
    logout(request)
    return redirect('/')
def Del(request):
    chatInfo.objects.filter(Q(userName = request.user.username)|Q(senderName = request.user.username)).delete()
    return redirect('userApp:home')