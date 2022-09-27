from django.urls import include, path
from todolist.views import delete_task, status_update, show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete_task/<str:name>/', delete_task, name='delete_task'),
    path('status-update/<str:name>/', status_update, name='status_update'),
]