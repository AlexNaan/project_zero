from django.urls import path,re_path
from . import views

urlpatterns = [

    path('', views.listOrganization),
    path('doc/', views.listDoc),
    path('employees/', views.listEmployee),
    path('employees/<str:Symbol>/<str:Page>/', views.listEmployee),
    path('employees/<str:Symbol>/', views.listEmployee),
    path('<str:idOrganization>/', views.listSubunit),
    path('<str:idOrganization>/<str:idSubunit>/', views.listStaff),
    path('<str:idOrganization>/<str:idSubunit>/<str:idEmployee>/', views.employee),

]
