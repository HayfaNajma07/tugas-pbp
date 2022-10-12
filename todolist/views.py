import datetime
from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist_user = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': data_todolist_user,
        'user_name': request.user
    }
    return render(request, "todolist.html", context)

def delete_task(request,id):
    task = Task.objects.filter(user=request.user).get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')

def set_status(request,id):
    task = Task.objects.filter(user=request.user).get(pk=id)
    if task.is_finished == False:
        task.is_finished = True
    else:
        task.is_finished = False

    task.save()
    return redirect('todolist:show_todolist')

def add_todolist(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        add_todolist = Task(
            user = request.user,
            title = title,
            description = description,
        )
        add_todolist.save()
        return redirect('todolist:show_todolist')
    return render(request, 'addtodolist.html')

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
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

@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task_ajax(request):
    if request.method == 'POST':
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        task = Task(user=user, date=date, title = title, description = description)
        task.save()

        output = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
                'date':task.date,
            }
        }
        return JsonResponse(output)

@csrf_exempt
def delete_task_ajax(request,id):
    task = Task.objects.filter(pk=id)   
    task.delete()
    return JsonResponse({"task": "todolist dihapus"})