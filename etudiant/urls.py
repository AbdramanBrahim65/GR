from django.conf.urls.static import static
from django.urls import path
from etudiant.views import home,ajout_views,modifier_views,supprimer_views,details_views
from GR import settings

urlpatterns = [
    path('',home,name='home'),
    path('ajout/',ajout_views,name='ajout'),
    path('modifier/<str:pk>',modifier_views,name='modifier'),
    path('supprimer/<str:pk>/',supprimer_views,name='supprimer'),
    path('details/<str:pk>',details_views,name='details'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
