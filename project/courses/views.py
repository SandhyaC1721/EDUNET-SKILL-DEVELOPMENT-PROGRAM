from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Course
from .models import Enrollment
from .models import Course, Enrollment
from django.shortcuts import get_object_or_404, redirect


def home(request):
    return render(request, 'courses/home.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'courses/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'courses/login.html')

@login_required
def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'courses/dashboard.html', {'courses': courses})
@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )

    return redirect('dashboard')