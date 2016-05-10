from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello_world, name='hello'),
    url(r'^desarrollador/registrar$', views.new_developer, name='new'),
    url(r'^desarrollador/(?P<name>[\w-]+)$', views.developer, name='developer'),
]