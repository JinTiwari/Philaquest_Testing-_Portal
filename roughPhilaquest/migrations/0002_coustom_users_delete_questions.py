# Generated by Django 4.1.1 on 2022-10-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coustom_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('USERNAME_FIELD', models.EmailField(max_length=254, unique=True)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Student_Class', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
