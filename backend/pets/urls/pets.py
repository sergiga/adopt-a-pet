from django.conf.urls import url
from pets.views import pets

urlpatterns = [
    url(r'^pets/$', pets.PetList.as_view()),
    url(r'^pets/(?P<pet_id>[0-9]+)/$', pets.PetDetail.as_view()),
]