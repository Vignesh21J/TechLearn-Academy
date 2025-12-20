from django.shortcuts import render

from academy.models import Course, Trainer, Student

def Home(request):

    courses = Course.objects.all()
    courses_count = courses.count()

    trainers = Trainer.objects.all()
    trainers_count = trainers.count()

    students = Student.objects.all()
    students_count = students.count()

    context = {
        'courses_count':courses_count,
        'trainers_count':trainers_count,
        'students_count':students_count
    }

    return render(request, "home.html", context)