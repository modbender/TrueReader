from django.urls import path

from . import views

urlpatterns = [
    path('change_theme/', views.change_theme, name='change_theme')
]
