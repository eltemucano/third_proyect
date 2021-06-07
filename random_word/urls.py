from django.urls import path, include
from . import views
# En esta sección defines las redirecciones a la vista
urlpatterns = [
    path('',views.redirige),
     path('random_word',views.index),
     path('random_word/reset',views.reset),

]