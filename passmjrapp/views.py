from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import OrderFilter
import random
import string


###################################################################
####################### Authorization #############################

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created successfully for: ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') # we get it from login.html name='username'
            password = request.POST.get('password') # we get it from login.html name="password"
            user = authenticate(request, username=username, password=password) # comparing values with db
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#################################################################

@login_required(login_url='login')
def home(request):
    loggeduser = request.user
    userid = loggeduser.id
    accounts = PasswordAccount.objects.filter(user=loggeduser)
    myFilter = OrderFilter(request.GET, queryset=accounts)
    accounts = myFilter.qs
    context = {'accounts':accounts, 'user':request.user, 'myFilter':myFilter }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = CreatePassForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('home')
    else:
        form = CreatePassForm()
    context = {'form':form}
    return render(request, 'create.html', context)

# @login_required(login_url='login')
# def create(request):
#     if request.method == 'GET':
#         return render(request, 'create.html', {'form':CreatePassForm})
#     else:
#         try:
#             form = CreatePassForm(request.POST)
#             newform = form.save(commit=False)
#             newform.user = request.user
#             newform.save()
#             return redirect('home')
#         except ValueError:
#             return render(request, 'create.html', {'form':CreatePassForm(), 'error':'Bad data passed in. Try again.'})



@login_required(login_url='login')
def update(request, pk):
    data = PasswordAccount.objects.get(id=pk)
    form = UpdatePassForm(instance=data)
    if request.method == 'POST':
        form = UpdatePassForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update.html', context)


@login_required(login_url='login')
def delete(request, pk):
    data = PasswordAccount.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/')
    context = {'item': data}
    return render(request, 'delete.html', context)

@login_required(login_url='login')
def view(request, pk):
    data = PasswordAccount.objects.get(id=pk)
    context = {'data':data}    
    return render(request, 'view.html',context)


#################################################
################## GENERATE Password ############

def passwordcreate(request):    
    characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
         characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length', "13"))
    password = ""
    form = CreatePassForm()
    for x in range(length):
        password += random.choice(characters)
    return render(request,'create.html', {'password': password, 'form':form})


@login_required(login_url='login')
def passgenerate(request):
    context = {}
    return render(request, 'passgenerate.html', context)