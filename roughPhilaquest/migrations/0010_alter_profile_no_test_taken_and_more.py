# Generated by Django 4.1.1 on 2022-10-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0009_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='No_Test_Taken',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Student_class',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
