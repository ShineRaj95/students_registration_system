from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User





""" function to show login form and on form submission check if 
username and password submitted matches a user in the database.
If credentials matches a user mark the user as logged in session
"""

def login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    auth_login(request,user)
                    return redirect('/')
            else:
                message=messages.add_message(request, messages.ERROR, 'username/password does not match.')
                return redirect('/login/')
        else:
            message=messages.add_message(request, messages.ERROR, 'Something went wrong')
            return redirect('/login/')

    else:
        form=LoginForm()
        context={'form':form }
        return render(request,'login.html',context)

