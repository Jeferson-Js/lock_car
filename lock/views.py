from django.shortcuts import render
from .carros_data import carros_localiza


# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    return render(request, 'confirmada.html')



def pagina_404(request, exception):
    return render(request, '404.html', status=404)