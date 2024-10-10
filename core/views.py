from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Tai Khoan Hop Le')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email hop le')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'User Hop Le')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password = password)
                user.save()
                
                # log user in
                user_login = auth.authenticate(username=username,password = password)
                auth.login(request,user_login)
                return redirect('/')
        else:
            messages.info(request, 'Mat Khau khong dung')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def bookticket(request):
    return render(request, 'book-ticket.html')

def seat(request):
    return render(request, 'seat.html')