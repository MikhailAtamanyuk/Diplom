from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', BlogCity.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('logoutuser/', auth_views.LogoutView.as_view(template_name='blog/index.html'), name='logoutuser'),
]