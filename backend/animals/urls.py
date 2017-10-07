from django.conf.urls import url
from animals import views

urlpatterns = [
    url(r'^animals/$', views.AnimalList.as_view()),
]