from django.urls import path
from . import views
urlpatterns = [
# Обработчики действий со статьями.
    path('', views.user_login, name='login'),
    path('exit', views.user_exit, name='login'),
]
