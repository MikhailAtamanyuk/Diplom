"""tourizm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from pesonal_account import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('lk/', views.lk, name='lk'),
    path('edit/', views.lk_edit, name='edit'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('crm/', views.crm, name='crm'),
    path('thanks_page/', views.thanks_page, name='thanks_page'),
    path('weather/', views.weather, name='weather'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
