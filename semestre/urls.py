from django.urls import path
from semestre.views import home_semestre,ajouter_semestre,modifier_semestre,supprimer_semestre,detail_semestre

urlpatterns = [
    path('home_semestre/',home_semestre,name='home_semestre'),
    path('ajouter_semestre/',ajouter_semestre,name='ajouter_semestre'),
    path('detail_semestre/<str:pk>/',detail_semestre,name='detail_semestre'),
    path('modifier_semestre/<str:pk>/',modifier_semestre,name='modifier_semestre'),
    path('supprimer_semestre/<str:pk>/',supprimer_semestre,name='supprimer_semestre'),
]