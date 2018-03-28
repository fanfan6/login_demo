from django.conf.urls import url

from views import manager, general


urlpatterns = [
    url(r'^manager', manager),
    url(r'^general', general),
]
