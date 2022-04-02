from django.urls import path
from parcours.views import home_parcours,ajouter_parcours,modifier_parcours,supprimer_parcours,detail_parcours

urlpatterns = [
    path('home_parcours/',home_parcours,name='home_parcours'),
    path('ajouter_parcours/',ajouter_parcours,name='ajouter_parcours'),
    path('detail_parcours/<str:pk>/',detail_parcours,name='detail_parcours'),
    path('modifier_parcours/<str:pk>/',modifier_parcours,name='modifier_parcours'),
    path('supprimer_parcours/<str:pk>/',supprimer_parcours,name='supprimer_parcours'),
]