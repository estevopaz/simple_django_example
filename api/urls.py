from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.add_new, name='new'),
    url(r'^news$', views.news, name='news'),
]
