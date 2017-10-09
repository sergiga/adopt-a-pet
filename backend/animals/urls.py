from django.conf.urls import url
from animals import views

urlpatterns = [
    url(r'^animals/$', views.AnimalList.as_view()),
    url(r'^animals/(?P<animal_id>[0-9]+)/$', views.AnimalDetail.as_view()),
]