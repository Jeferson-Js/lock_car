from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def novidades(request):
    card_range = range(20)
    carros_localiza = [
        {
            "nome": "Sedan Compacto",
            "cor": "Prata",
            "imagem": "img/ARGO.png"
        },
        {
            "nome": "SUV Médio",
            "cor": "Preto",
            "imagem": "img/carros.png"
        },
        {
            "nome": "Hatchback Esportivo",
            "cor": "Vermelho",
            "imagem": "img/carros.png"
        },
        {
            "nome": "Minivan Familiar",
            "cor": "Branco",
            "imagem": "img/carros.png"
        },
        {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
         {
            "nome": "Caminhonete",
            "cor": "Azul",
            "imagem": "img/carros.png"
        },
        # ... adicione informações de cor e imagem para os outros carros ...
    ]

    return render(request, 'novidades.html', {'card_range': card_range, 'carros_localiza': carros_localiza})

def reservas(request):
    return render(request, 'reservas.html')

def suporte(request):
    return render(request, 'suporte.html')

def promocoes(request):
    return render(request, 'promocoes.html')

def detalhes(request, id):
    card_number = int(id) + 1
    return render(request, 'detalhes.html', {'id': card_number})


def pagina_404(request, exception):
    return render(request, '404.html', status=404)