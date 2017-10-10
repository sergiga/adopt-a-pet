from django.conf.urls import url
from pets.views import adoptions

urlpatterns = [
    url(r'^adoptions/users/(?P<adopter_id>[0-9]+)/$', adoptions.AdoptionList.as_view()),
    url(r'^adoptions/pets/(?P<pet_id>[0-9]+)/$', adoptions.AdoptionList.as_view()),
    url(r'^adoptions/users/(?P<adopter_id>[0-9]+)/pets/(?P<pet_id>[0-9]+)/$', adoptions.AdoptionDetail.as_view()),
    url(r'^adoptions/pets/(?P<pet_id>[0-9]+)/users/(?P<adopter_id>[0-9]+)/$', adoptions.AdoptionDetail.as_view()),
]