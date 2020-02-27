from django.shortcuts import render
from .models import Students
from login.views import login
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout




"""Function to show manage students page. This page lists all students.
List has option to edit or delete student details by clicking the edit
or delete button in the row coresponding to the student. Clicking the 
add button user will be able to  add student"""
@login_required(login_url="/login/")
def student_listing_page(request):
    all_students = Students.objects.all()
    context={ 'students':all_students }
    return render(request,'list-students.html',context)




"""Function to add student"""
@login_required(login_url="/login/")
def add_students(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            phone = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            course = form.cleaned_data['course']
            

            student_object = Students()
            student_object.name = name
            student_object.age = age
            student_object.email = email
            student_object.phone = phone
            student_object.address = address
            student_object.gender = gender
            student_object.course = course

            try:
                student_object.save()
            except:
                context={'form':form}
                message=messages.add_message(request, messages.ERROR, 'Email or mobile number already exist')
                return render(request,'add-student.html',context)
            message=messages.add_message(request, messages.SUCCESS, 'Added student successfully')
            return redirect('/')
        else:
            context={'form':form}
            return render(request,'add-student.html',context)

    else:
        form=RegistrationForm()
        context={'form':form}
        return render(request,'add-student.html',context)




"""Function to  edit student"""
@login_required(login_url="/login/")
def edit_students(request,student_id):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            student=Students.objects.get(id=student_id)
            student.name=form.cleaned_data['name']
            student.email = form.cleaned_data['email']
            student.age = form.cleaned_data['age']
            student.phone = form.cleaned_data['phone_number']
            student.address = form.cleaned_data['address']
            student.gender = form.cleaned_data['gender']
            student.course = form.cleaned_data['course']
            student.save()

            message=messages.add_message(request, messages.SUCCESS, 'Updated successfully')
            return redirect('/')
        else:
            context={'form':form}
            return render(request,'edit-student.html',context)

    else:      
        try:
            student=Students.objects.get(id=student_id)
            form = RegistrationForm(initial={"name":student.name,"email":student.email,"age":student.age,"phone_number":student.phone,"address":student.address,"gender":student.gender,"course":student.course}) 
            context={'form':form,'sid':student_id}
            return render(request,'edit-student.html',context)
        except Students.DoesNotExist:
            message=messages.add_message(request, messages.ERROR, 'Student does not exist')
            return render(request,'edit-student.html')




"""Function to delete student"""
@login_required(login_url="/login/")
def delete_student(request):
    if request.method == "POST":
        student_id=request.POST.get('studentId')
        student=Students.objects.get(id=student_id)
        student.delete()
        return JsonResponse('successfully deleted',safe=False)




"""Function get list of students filtered by name"""
@login_required(login_url="/login/")
def filter_students(request):
    if request.method == 'POST':
        pass_name =request.POST.get('userName')
        filtered_user_list=Students.objects.filter(name__icontains=pass_name)
        user_list=serializers.serialize('json',filtered_user_list)

        return JsonResponse(user_list,safe=False)
    



""" function get list of students filtered by course """

@login_required(login_url="/login/")
def filter_students_by_course(request):
    if request.method == 'POST':
        pass_course =request.POST.get('course')
        filtered_user_list=Students.objects.filter(course__icontains=pass_course)
        user_list=serializers.serialize('json',filtered_user_list)

        return JsonResponse(user_list,safe=False)
    



""" function to make the superuser logout """

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect('login/')
    
