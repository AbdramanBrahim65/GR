from django.urls import path
from ue.views import home_ue,ajouter_ue,modifier_ue,supprimer_ue,detail_ue

urlpatterns = [
    path('home_ue/',home_ue,name='home_ue'),
    path('ajouter_ue/',ajouter_ue,name='ajouter_ue'),
    path('detail/<str:pk>/',detail_ue,name='detail'),
    path('modifier_ue/<str:pk>/',modifier_ue,name='modifier_ue'),
    path('supprimer_ue/<str:pk>/',supprimer_ue,name='supprimer_ue'),
]