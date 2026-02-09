from django.shortcuts import render

# Create your views here.
def student_list(request):
    # Sample data - normally this could come from a database query
    students = [
        {'name': 'Sandhya', 'course': ' Information Science'},
        {'name': 'Gowthami', 'course': 'Computer Science'},
        {'name': 'Meghana', 'course': 'Aritificial Intelligence'}
    ]
        # Context dictionary - keys will become variable names in the template
    context = {'students': students}
    # Render the template and send the data
    return render(request, 'profiles/student_list.html', context)
