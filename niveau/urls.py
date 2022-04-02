from django.urls import path
from niveau.views import home_niveau,ajouter_niveau,modifier_niveau,supprimer_niveau,detail_niveau

urlpatterns = [
    path('home_niveau/',home_niveau,name='home_niveau'),
    path('ajouter_niveau/',ajouter_niveau,name='ajouter_niveau'),
    path('detail_niveau/<str:pk>/',detail_niveau,name='detail_niveau'),
    path('modifier_niveau/<str:pk>/',modifier_niveau,name='modifier_niveau'),
    path('supprimer_niveau/<str:pk>/',supprimer_niveau,name='supprimer_niveau'),
]