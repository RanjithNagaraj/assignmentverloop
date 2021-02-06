from django.urls import path

from . import views


urlpatterns = [

    path('', views.latnlng, name='latlng'),
    path('reverse', views.reverse, name='reverse'),
]