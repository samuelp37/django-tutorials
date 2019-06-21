from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('insert_article/', views.insert_article, name='insert_article'),
    path('insert_contact/', views.nouveau_contact, name='insert_contact'),
    path('voir_contacts/', views.voir_contacts, name='voir_contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
