from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('help/', views.help, name="help"),
    path('sexuais/', views.sexuais, name="sexuais"),
    path("post/<int:id>",views.post ,name="post")
]
