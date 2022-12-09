from django.urls import path
from . import views


urlpatterns = [
    path('',views.spot,name='spot'),
    path('',views.spot,name='logout')
]
