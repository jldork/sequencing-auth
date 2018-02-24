from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.auth),
    url(r'^authorize', views.auth_callback),
    url(r'^authorization-approved', views.api, name="api"),
]
