from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def novidades(request):
    card_range = range(20)
    return render(request, 'novidades.html', {'card_range': card_range})

def reservas(request):
    return render(request, 'reservas.html')

def suporte(request):
    return render(request, 'suporte.html')

def promocoes(request):
    return render(request, 'promocoes.html')

def detalhes(request, id):
    return render(request, 'detalhes.html', {'id': id})

def pagina_404(request, exception):
    return render(request, '404.html', status=404)