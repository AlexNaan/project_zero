# Generated by Django 3.2.8 on 2021-10-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_1c', '0004_typeaccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='listusers',
            name='role_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users_1c.typeaccess'),
        ),
    ]
