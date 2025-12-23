from django.shortcuts import render
from .models import Course, Trainer, Student

from django.db import connection

# Create your views here.
def Courses(request):
    courses = Course.objects.all()

    return render(request, 'academy/courses.html', {'courses':courses})

def Trainers(request):

    # trainers = Trainer.objects.all()
    # return render(request, 'academy/trainers.html', {'trainers':trainers})


    # Django's Forward Lookup and Reverse Lookup.

    # Forward Lookup: means accessing the course name from the trainer's expertise field.

    # Reverse Lookup: means instead of accessing the instagram post from that post's comment.
                    # We try to access all comments from a instagram post.

    # We Tried below commented code as Brute force. This tried technique is called Forward-Lookup.
    # For Ex: Forward-Lookup: means accessing the instagram post from that post's comment.

    # In our case, it means accessing the course name from trainer's expertise field.


    




    # trainers = Trainer.objects.all()

    # # for trainer in trainers:
    # #     print(trainer.first_name)

    # for trainer in trainers:
    #     print(trainer.first_name, trainer.expertise.name)

    # for query in connection.queries:
    #     print(query['sql'])

    # print(f'Total no of queries executed: {len(connection.queries)}, which is n+1 numb of queries [ no of trainers + 1].')


    # OPTIMAL (Forward-Lookup: means accessing the course name from the trainer's expertise field.)

    # trainers = Trainer.objects.select_related('expertise')   # ('') here give foreign key's column name.
    # for trainer in trainers:
    #     print(trainer.first_name, trainer.expertise.name)
    # print('\n\n')

    # for query in connection.queries:
    #     print(query['sql'])

    # print('\n\n')

    # print(f'Total no of queries executed: {len(connection.queries)}')
    # print('\n\n')

    # trainers = Trainer.objects.all()

    trainers = Trainer.objects.select_related('expertise')   # ('') here give foreign key's column name.
    # select_related('') here will always takes the ForeignKey field name defined on the model.

    return render(request, 'academy/trainers.html', {'trainers':trainers})


def Students(request):
    # students = Student.objects.all()

    students = Student.objects.select_related('enrolled_course', 'trainer')

    return render(request, 'academy/students.html', {'students':students})