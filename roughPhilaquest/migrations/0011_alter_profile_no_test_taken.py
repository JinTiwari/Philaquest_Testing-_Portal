# Generated by Django 4.1.1 on 2022-10-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roughPhilaquest', '0010_alter_profile_no_test_taken_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='No_Test_Taken',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
