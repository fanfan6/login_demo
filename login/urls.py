from django.conf.urls import url

from views import LoginView, index, logout, success


urlpatterns = [
    url(r'^login', LoginView.as_view()),
    url(r'^logout', logout),
    url(r'^success', success),
    url(r'^$', index),
]
