from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse

# Create your views here.
def courses_list(request):
    courses_list = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses_list': courses_list})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}

    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    

    context['form'] = form
    context['course'] = course
    return render(request, 'courses/course_detail.html', context)

