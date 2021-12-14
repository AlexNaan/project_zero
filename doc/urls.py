from django.urls import path,re_path
from . import views
urlpatterns = [

    path('docinfo/<str:number>/<str:str_data>/<int:type_doc>', views.selected_docinfo, name='selected_docinfo'),
    path('all/', views.doc_all, name='doc_all'),
    path('1/', views.doc_1, name='doc_1'),
    path('2/', views.doc_2, name='doc_2'),
    path('3/', views.doc_3, name='doc_3'),
    path('4/', views.doc_4, name='doc_4'),
    path('5/', views.doc_5, name='doc_5'),

]
