# Generated by Django 4.1.1 on 2022-10-18 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0003_alter_coustom_users_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coustom_users',
            name='last_login',
        ),
    ]
