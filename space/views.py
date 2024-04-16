from django.shortcuts import render

# Create your views here.

def index(request):

    dados = {1:{'nome': 'Galaxia X014',
                'legenda': 'NASA / WEB / JAMES WEBB '},
             2:{'nome': 'Galaxia G546', 
                'legenda': 'NASA / HUUB / WEB'}   
             }

    return render(request, 'space/index.html', {'cards': dados} )

def imagem(request):
    return render(request, 'space/imagem.html')


