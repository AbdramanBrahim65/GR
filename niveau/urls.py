from django.urls import path
from niveau.views import home_niveau,ajouter_niveau,modifier_niveau,supprimer_niveau,detail_niveau,home_Nparcours,ajouter_Nparcours,modifier_Nparcours,supprimer_Nparcours,detail_Nparcours

urlpatterns = [
    path('home_niveau/',home_niveau,name='home_niveau'),
    path('ajouter_niveau/',ajouter_niveau,name='ajouter_niveau'),
    path('detail_niveau/<str:pk>/',detail_niveau,name='detail_niveau'),
    path('modifier_niveau/<str:pk>/',modifier_niveau,name='modifier_niveau'),
    path('supprimer_niveau/<str:pk>/',supprimer_niveau,name='supprimer_niveau'),
    path('home_Nparcours/',home_Nparcours,name='home_Nparcours'),
    path('ajouter_Nparcours/',ajouter_Nparcours,name='ajouter_Nparcours'),
    path('detail_Nparcours/<str:pk>/',detail_Nparcours,name='detail_Nparcours'),
    path('modifier_Nparcours/<str:pk>/',modifier_Nparcours,name='modifier_Nparcours'),
    path('supprimer_Nparcours/<str:pk>/',supprimer_Nparcours,name='supprimer_Nparcours'),
]