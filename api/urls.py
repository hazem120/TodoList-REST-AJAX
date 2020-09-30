from django.urls import path  
from . import views 
urlpatterns = [
    path('task-list' , views.taskList , name = 'tasks'),
    path('task-create' , views.taskCreate , name = 'task-create'),
    path('task/<int:id>' , views.taskDetail , name = 'task'),
    path('task/<int:id>/update' , views.taskUpdate , name = 'task-update'),
    path('task/<int:id>/delete' , views.taskDelete , name = 'task-delete'),



]
