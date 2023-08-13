from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .carros_data import carros_localiza
from .dados_users import usuario
import datetime
import geocoder


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')  # Substitua 'dashboard' pelo nome da URL da página após o login
        else:
            print('erro!')
   return render(request, 'login.html')

def novidades(request):
    card_range = range(20)
    return render(request, 'novidades.html', {'card_range': card_range, 'carros_localiza': carros_localiza})


def reservas(request):
    return render(request, 'reservas.html')


def suporte(request):
    return render(request, 'suporte.html')


def promocoes(request):
    return render(request, 'promocoes.html')


def detalhes(request, id):
    id = int(id)
    carro = carros_localiza[id]
    return render(request, 'detalhes.html', {'carro': carro, 'carros_localiza': carros_localiza})


def confirmada(request):
    dados = usuario
    hora_atual = datetime.datetime.now()
    cidade = "São Paulo, Brazil"
    localizacao = geocoder.osm(cidade)

    if localizacao.ok:
        cidade_info = {
            "nome": localizacao.city,
            "estado": localizacao.state,
            "pais": localizacao.country
        }
    else:
        cidade_info = None
    return render(request, 'confirmada.html', {'usuario': dados, 'hora_atual': hora_atual, 'cidade_info': cidade_info})

