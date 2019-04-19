from django.shortcuts import render
from django.http import HttpResponse
import paramiko
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def detail(request,num,num2):
    return HttpResponse("detail-%s-%s"%(num,num2))

from .models import Grade,Student
def grade(request):
    gradeList = Grade.objects.all()
    return render(request,'ansible/grade.html',{"grades":gradeList})

def studentByGradeId(request,id):
    ssh = paramiko.SSHClient()
    print("--------1")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("--------2")
    ssh.connect('172.16.229.133', username='root', password='123456')
    print("--------3")
    stdin, stdout, stderr = ssh.exec_command("ansible all -m ping")
    print("--------4")
    print(stdout.readlines())
    ssh.close()
    print("--------5")
    grade = Grade.objects.get(pk=id)
    studentList = grade.student_set.all()
    return render(request,'ansible/grade.html',{"students":studentList})

def student(request):
    #studentList = Student.objects.all()
    studentList = Student.stuObj2.all()
    return render(request,'ansible/student.html',{'students':studentList})