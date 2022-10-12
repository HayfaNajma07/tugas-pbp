from django.urls import path
from todolist.views import add_task_ajax, add_todolist, delete_task, delete_task_ajax, set_status, show_json, show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', add_todolist, name='add_todolist'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('set_status/<int:id>/', set_status, name='set_status'),
    path('json/', show_json, name='show_json'),
    path('add_task_ajax/', add_task_ajax, name='add_task_ajax'),
    path('delete/<int:id>/', delete_task_ajax, name='delete_task_ajax'),
]