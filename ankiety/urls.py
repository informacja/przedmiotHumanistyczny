from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home),
    path('wypelnij/', views.wypelnij),
    path('wyniki/', views.wyniki),
    path('dziekuje/', views.dziekuje, name='dziekuje'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
