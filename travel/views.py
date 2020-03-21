from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Import all the models created so far
from travel.models import Traveler

# import User model
from django.contrib.auth.models import User

def index(request):
    # Testing http request object inside a view function
    print('*********** Testing request obj ************')
    print('request:' , request)
    print('request.headers: ', request.headers)
    print('request.headers["host"]:', request.headers['host'])
    print('request.method: ', request.method)
    print('request.user:' , request.user)
    print('*******************************')

    if request.method == "GET":
        #if request.user.is_authenticated:
        user = request.user
            #all_problems = Problem.objects.all()   # all_problems is a list object [   ]

        return render(request, "travel/index.html", {"user":user})
        #else:
        #    return redirect("travel:login")
    else:
        return HttpResponse(status=500)

def dashboard(request):
    # retieve user, my_problems, my-scripts
    # builds my_problems_scripts dict
    # renders dashboard.html
    # each problem should have a link show more details of a particular problem,
    # this link starts route show_my_problem

    # Testing http request object inside a view function
    print('*********** Testing request obj ************')
    print('request:' , request)
    print('request.headers: ', request.headers)
    print('request.headers["host"]:', request.headers['host'])
    print('request.method: ', request.method)
    print('request.user:' , request.user)
    print('*******************************')

    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("travel:login")
        else:
            #my_problems = Problem.objects.filter(coder=user.coder.id)   # Problem table has a coder field (FK)
            #my_scripts =  Script.objects.filter(coder=user.coder.id)

            print('*********** Testing objs retrieved from DB ************')
            #print('my_problems:', my_problems)
            #print('my_scripts:', my_scripts)
            print('*******************************')

            return render(request, "travel/dashboard.html")

def create(request):
    pass

def signup(request):
    pass

def login_user(request):
    pass

def login_view(request):
    pass

def logout_view(request):
    pass
