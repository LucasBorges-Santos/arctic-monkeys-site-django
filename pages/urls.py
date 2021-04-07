from django.urls import path
from . import views

app_name = 'pages'

# para views como classes
"""urlpatterns = [
    path('sobre/', views.sobre.as_view(), name='sobre'),
    path('musicas/', views.musicas.as_view(), name='musicas'),
]"""


# para views como funções
urlpatterns = [
    path('sobre/', views.sobre, name='sobre'),
    path('musicas/', views.musicas, name='musicas'),
]

# Utilizando 'name'

"""
Para utilizarmos 'name', para redirecionamento dentro do nosso template, precisamos colocar nosso 'href' da seguinte forma:
    
    <a href="{% url '<app>:<name>' %}">

Como exemplo, para acessarmos a pagina sobre, seria da sgeuinte forma:

    <a href="{% url 'pages:sobre'%}">
"""