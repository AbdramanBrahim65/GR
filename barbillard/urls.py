from django.urls import path
from barbillard.views import accueil,barbillard_views,synthese,ue

urlpatterns = [
    path('',accueil,name='accueil'),
    path('barbillard/',barbillard_views,name='barbillard'),
    path('synthese/',synthese,name='synthese'),
    path('ue/',ue,name='ue'),
]