from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about_us', views.aboutUS, name='aboutUS'),
    path('contactUS', views.aboutUS, name='contactUS'),
    path('services', views.aboutUS, name='services'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),

    path('salarie', views.salarie, name='salarie'),
    path('commercial', views.commercial, name='commercial'),
    path('managers', views.manager, name='managers'),

]