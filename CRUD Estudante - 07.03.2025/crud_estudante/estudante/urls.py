from django.urls import path 
from . import views

urlpatterns = [
    path('', views.listar_alunos),
    path('criar/', views.criar_aluno)
]