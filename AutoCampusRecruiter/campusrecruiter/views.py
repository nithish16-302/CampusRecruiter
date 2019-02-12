from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.utils import timezone

from django.views.decorators import csrf
from .forms import AddForm,AddStudents
from .models import Recruitment,Students
from django.contrib.auth import logout
from .utils import render_to_pdf
from django.views.generic import View





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

def studentReg(requests):
    return render(requests,"campusrecruiter/studentReg.html")

def success(requests):
    if requests.method == 'POST':
        django_form = AddStudents(requests.POST)
        if django_form.is_valid():
            new_student_name = django_form.data.get("stuName")
            new_college = django_form.data.get("collName")
            new_rollno = django_form.data.get("rollno")
            new_gpa = django_form.data.get("stugpa")
            Students.objects.create(
                student_name = new_student_name,
                student_coll = new_college,
                roll_no = new_rollno,
                student_gpa = new_gpa

            )

    return render(requests, 'campusrecruiter/success.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

class GeneratePdf(View):
    def get(self, *args, **kwargs):
        #data = {
           #  'today': timezone.now(),
            # 'amount': 39.99,
           # 'customer_name': 'Cooper Mann',
           # 'order_id': 1233434,
       # }
        pdf = render_to_pdf('campusrecruiter/invoice.html')
        return HttpResponse(pdf, content_type='application/pdf')

