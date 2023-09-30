from django.urls import path
from .views import *

urlpatterns = [

    # path('<int:code>/', index, name='index'),
    path('', page_404, name='404'),
    path('<int:code>/', index, name="index"),
    path('cooking_fish/', cooking_fish, name="cooking_fish"),
    path('404/', page_404, name='404'),
]