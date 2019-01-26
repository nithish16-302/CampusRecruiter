from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators import csrf
from .forms import AddForm
from .models import Recruitment,Students

# Create your views here.
def login(requests):
    c = {}
    return render(requests, 'campusrecruiter/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return render(request,'campusrecruiter/home.html')
    else:
        return render(request,'campusrecruiter/home.html')

def home(requests):
    College_list = Recruitment.objects.all()
    stulist = Students.objects.all()
    usern = requests.user.username
    return render(requests,"campusrecruiter/home.html",{'colleges': College_list,'stulist':stulist,'usern':usern})

def create(requests):
    if requests.method == 'POST':
        django_form = AddForm(requests.POST)
        if django_form.is_valid():
            new_college_name = django_form.data.get("collegeName")
            new_college_addr = django_form.data.get("colAddr")
            new_username    = requests.user.username
            Recruitment.objects.create(
                col_name=new_college_name,
                col_address=new_college_addr,
                username =new_username,
            )
            return render(requests, 'campusrecruiter/create.html')

def show(requests):
    studentslist = Students.objects.all()
    return render(requests,"campusrecruiter/show.html",{'studentlist':studentslist})