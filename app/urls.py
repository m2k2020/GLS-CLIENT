from django.urls import path
from .views import *

urlpatterns = [

    # path('<int:code>/', index, name='index'),
    path('', page_404, name='404'),
    path('<int:code>/', index, name="index"),
    path('test_page/', cooking_fish, name="test_page"),
    path('404/', page_404, name='404'),
]