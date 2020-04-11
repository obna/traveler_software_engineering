from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Import all the models created so far
from .models import Traveler, Location, Destination, Review, Comment

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
        if not user.is_authenticated:
            return redirect("travel:login")
        else:
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
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        traveler_yet = request.POST['coder_yet_checkbox']

        if username is not None and email is not None and password is not None: # checking that they are not None
            if not username or not email or not password: # checking that they are not empty
                return render(request, "travel/signup.html", {"error": "Please fill in all required fields"})
            if User.objects.filter(username=username).exists():
                return render(request, "travel/signup.html", {"error": "Username already exists"})
            elif User.objects.filter(email=email).exists():
                return render(request, "travel/signup.html", {"error": "Email already exists"})
            # save our new user in the User model
            user = User.objects.create_user(username, email, password)
            traveler = Traveler.objects.create(user= user, traveler_yet = traveler_yet).save()
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            # this logs in our new user, backend means that we are using the  Django specific auhentication and not 3rd party

        return redirect("travel:index")

    else:
        return redirect("travel:signup")

def signup(request):
    if request.user.is_authenticated:
        return redirect("travel:index")
    return render(request, 'travel/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not username or not password:
            return render(request, "travel/login.html", {"error":"One of the fields was empty"})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("travel:index")
        else:
            return render(request, "travel/login.html", {"error":"Wrong username or password"})
    else:
        return redirect("travel:index")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("travel:index")
    return render(request, 'travel/login.html')

def logout_view(request):
    logout(request)
    return redirect("travel:login")

def create_destination(request):
    pass

def show_destination(request, destination_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("travel:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            destination = get_object_or_404(Destination, pk=destination_id)
            reviews = Review.objects.filter(destination=destination_id)
            return render(request, "travel/show_destination.html", {"user":user, "destination":destination, "reviews":reviews})

def edit_destination(request, destination_id):
    pass

def update_destination(request, destination_id):
    pass

def delete_destination(request, destination_id):
    pass

def create_location(request):
    pass

def show_location(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("travel:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            location = get_object_or_404(Location, pk=location_id)
            destinations = Destination.objects.filter(location=location_id)

            return render(request, "travel/show_location.html", {"user":user, "location":location, "destinations":destinations})

def edit_location(request, location_id):
    pass

def update_location(request, location_id):
    pass

def delete_location(request, location_id):
    pass

def create_review(request, destination_id):
    pass

def show_review(request, review_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("travel:login")
        else:
            # make sure to import the fucntion get_object_or_404 from  django.shortcuts
            review = get_object_or_404(Review, pk=review_id)
            comments = Comment.objects.filter(review=review_id)

            return render(request, "travel/show_review.html", {"user":user, "review":review, "comments":comments})

def edit_review(request, review_id):
    pass

def update_review(request, review_id):
    pass

def delete_review(request, review_id):
    pass
