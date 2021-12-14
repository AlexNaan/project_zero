from django.urls import path,re_path
from . import views

urlpatterns = [

    
    path('photo/<str:idEmployee>/', views.getPhotoEmployee),
    path('certificate/<str:idCertificate>/', views.getCertificateEmploy),
]
