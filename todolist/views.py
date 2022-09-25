from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_task_todolist,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def create_task(request):
    if request.method == "POST":
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        new_task = Task(
            user = request.user,
            date = str(date.today()),
            title = judul,
            description = deskripsi, 
            is_finished = False
        )
        if (judul == "" or deskripsi == ""):
            messages.info(request, 'Silahkan masukkan Judul dan Deskripsi Task Anda!')
        else:
            new_task.save()
            return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response