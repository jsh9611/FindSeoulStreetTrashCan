from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'english_map'

urlpatterns = [
    url(r'^$', views.showmap_eng),
    url(r'^results/$', views.results_eng),
]