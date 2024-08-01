# Generated by Django 4.2.7 on 2024-08-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_adultregistration_studentregistration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.RemoveField(
            model_name='user', 
            name='is_student',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('employee', 'Employee')], default='student', max_length=10),
        ),
    ]
