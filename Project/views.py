import logging

from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

from Project.models import Student

logger = logging.getLogger('log')


@require_GET
def addStudent(request):
    sno = request.GET.get('sno')
    name = request.GET.get('name')
    stu = Student(sno=sno, name=name)
    stu.save()
    return JsonResponse(data={}, safe=False)


@require_GET
def selectStudent(request):
    sno = request.GET.get('sno')
    info = Student.objects.filter(sno=sno).first()
    print(info.name)
    return JsonResponse(data={}, safe=False)


def deleteStudent(request):
    sno = request.GET.get('sno')
    info = Student.objects.filter(sno=sno).first()
    info.delete()
    return JsonResponse(data={}, safe=False)


def updateStudent(request):
    sno = request.GET.get('sno')
    name = request.GET.get('name')
    stu = Student.objects.filter(sno=sno).first()
    stu.name = name
    stu.save()
    return JsonResponse(data={}, safe=False)
