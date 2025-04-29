"""
URL configuration for pass_manage_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from manager_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Index"),
    path('Home', views.home, name="Home"),
    path('About', views.about, name="About"),
    path('Contact', views.contact, name="Contact"),
    path('Register', views.signup, name="Register"),
    path('Login', views.signin, name="Authentication"),
    path('Forgot', views.verify, name="Verification"),
    path('Forgot/<str:value>', views.update, name="Update"),
    path('Logout', views.logout, name="Logout"),
    path('Dashboard', views.dashboard, name="Dashboard"),
    path('Dashboard/<str:name>', views.profile, name="Profile"),
    path('Dashboard/Add/<str:name>', views.add, name="Credentials"),
    path('Dashboard/Manage/<str:name>', views.all, name="Show_Credentials"),
    path('Dashboard/Settings/<str:name>', views.setting, name="Account"),
    path('Dashboard/Manage/<str:name>/<str:id>', views.controle, name="manage_Credentials"),
    path('Dashboard/Activity/<str:name>', views.activity, name="History"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
