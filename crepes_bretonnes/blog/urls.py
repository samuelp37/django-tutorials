from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('insert_article/', views.insert_article, name='insert_article'),
    path('insert_contact/', views.nouveau_contact, name='insert_contact'),
    path('voir_contacts/', views.voir_contacts, name='voir_contact'),
]
