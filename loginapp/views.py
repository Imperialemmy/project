
# def index(request):
#     # return render (request, 'index.html')
#     return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login details')
    return render(request, 'login.html', {'form': LoginForm})



def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    return redirect('/')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # first_name = request.POSTget('first_name')
#         # last_name = request.POSTget('last_name')
#         # email = request.POSTget('email')

#         user = auth.authenticate(username = username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, 'Invalid login details')
#     return render(request, 'register.html', {'form': RegisterForm})



# This is for the register page so immediately it registers it takes you to the homepage, so I created a homepage named homepage.html
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.save()

            # Logs the user in
            auth.login(request, user)
            return redirect('home')

    return render(request, 'register.html', {'form': RegisterForm})

def home(request):
    return render(request,'homepage.html')


