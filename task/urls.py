from django.urls import path,re_path
from . import views
urlpatterns = [

    path('info_task/<str:number>/<str:str_data>/execute', views.selected_exec, name='selected_exec'),
    path('info_task/<str:number>/<str:str_data>', views.selected_task, name='selected_task'),
    path('active/', views.task_active, name='task_active'),
    path('close/', views.task_close, name='task_close'),

]
