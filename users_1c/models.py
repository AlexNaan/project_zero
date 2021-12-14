from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ListUsers(models.Model):
    TypeAccess = (
        ('Security','Охрана труда'),
        ('Harmonization','Согласование документов'),
        ('Harmonization-Security','Охрана труда и согласовнаие документов'),
        )
    name_users_1c = models.CharField(max_length=250)
    kod_users_1c = models.CharField(max_length=11,default='00000000000')
    slug = models.SlugField(max_length=250)
    user_web = models.ForeignKey(User,on_delete=models.CASCADE,related_name='name_users_1c')
    user_role = models.CharField(max_length=50,
                                      choices=TypeAccess,
                                      default='Security')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-user_web',)

    def __str__(self):
        return self.name_users_1c


