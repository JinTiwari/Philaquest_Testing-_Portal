# Generated by Django 4.1.1 on 2022-10-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0012_questionpaper_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='Name',
            field=models.CharField(max_length=20),
        ),
    ]