# Generated by Django 4.1.1 on 2022-10-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='No_Test_Taken',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Student_class',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='response_test1',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
