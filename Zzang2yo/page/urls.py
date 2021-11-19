from django.urls import path
from . import views

urlpatterns = [
    # path('map/', views.maps),
    path('', views.main),
]