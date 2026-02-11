from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Student
# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'profiles/student_list.html', {'students': students})
# Show details of one student
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'profiles/student_detail.html', {'student': student})
