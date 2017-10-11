from django.conf.urls import url
from pets.views import messages

urlpatterns = [
    url(r'^$', messages.MessageList.as_view()),
]