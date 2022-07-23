from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('citys/',views.citys, name='citys'),
    path('districts/',views.districts, name='districts'),

]