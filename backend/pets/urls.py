from django.conf.urls import url
from pets import views

urlpatterns = [
    url(r'^pets/$', views.PetList.as_view()),
    url(r'^pets/(?P<pet_id>[0-9]+)/$', views.PetDetail.as_view()),
    url(r'^adoptions/users/(?P<adopter_id>[0-9]+)/$', views.AdoptionList.as_view()),
    url(r'^adoptions/pets/(?P<pet_id>[0-9]+)/$', views.AdoptionList.as_view()),
    url(r'^adoptions/users/(?P<adopter_id>[0-9]+)/pets/(?P<pet_id>[0-9]+)/$', views.AdoptionDetail.as_view()),
    url(r'^adoptions/pets/(?P<pet_id>[0-9]+)/users/(?P<adopter_id>[0-9]+)/$', views.AdoptionDetail.as_view()),
]