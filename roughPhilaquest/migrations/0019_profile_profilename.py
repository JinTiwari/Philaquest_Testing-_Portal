# Generated by Django 4.1.1 on 2022-10-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0018_profile_test1_profile_test2_profile_test3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Profilename',
            field=models.CharField(default='test', max_length=25),
        ),
    ]
