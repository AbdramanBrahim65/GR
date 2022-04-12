from django.urls import path
from .views import home_eval,ajouter_eval,modifier_eval,supprimer_eval,detail_eval

urlpatterns = [
    path('home_eval/',home_eval,name='home_eval'),
    path('ajouter_eval/',ajouter_eval,name='ajouter_eval'),
    path('detail_eval/<str:pk>/',detail_eval,name='detail_eval'),
    path('modifier_eval/<str:pk>/',modifier_eval,name='modifier_eval'),
    path('supprimer_eval/<str:pk>/',supprimer_eval,name='supprimer_eval'),
]