from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    url(r'^$', views.showmap),
    url(r'^results/$', views.results),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # path('index3/', views.index3),
]