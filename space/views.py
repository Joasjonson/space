from django.shortcuts import render, get_object_or_404
from space.models import Fotografia

# Create your views here.

def index(request):
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'space/index.html', {'cards': fotografia} )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'space/imagem.html', {"fotografia": fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_buscar = request.GET["buscar"]                                         # Funçao de Buscar na Barra de pesquisa
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)           # Retorna dados de acordo com a palavra digitada no campo de busca

    return render(request, "buscar.html", {"cards": fotografias})