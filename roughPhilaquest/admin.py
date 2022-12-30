from django.contrib import admin

#registering models here on own

from .models import Profile , QuestionPaper , Questions

admin.site.register(Profile)
admin.site.register(QuestionPaper)
admin.site.register(Questions)