from django.urls import path
from compte.views import accessPage,logoutUser

urlpatterns = [
    path('login/',accessPage,name='login'),
    path('quitter/',logoutUser,name='quitter')
]
