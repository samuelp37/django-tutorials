from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("""
    <h1>Bienvenue sur mon blog !</h1>
    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def view_article(request, id_article):
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )
