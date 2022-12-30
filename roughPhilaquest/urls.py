"""roughPhilaquest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.loginPaage  , name = "Welcome"),
    path('signup' , views.signUp , name = "signUp"),
    path('confirmations' , views.confirmations , name="confirmations"),
    path('login', views.loginformfill , name="login"),
    path('login2', views.handleLogin , name="handleLogin"),
    path('Udashboard/logout', views.handleLogout , name="handleLogout"),
    path('Udashboard', views.dashboard , name="Udashboard"),
    path('Udashboard/test', views.testPage , name="TestPage"),
    path('Udashboard/taketest', views.taketest , name="TestTake"),
    path('Udashboard/submitTest', views.checkAnswers , name="SubmitTest"),
    path('Udashboard/results', views.results , name="getResults"),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


