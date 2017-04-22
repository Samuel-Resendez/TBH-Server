from django.conf.urls import url
from TBHServer import views


urlpatterns = [
    url(r'^entries/$',views.EntryList),
    url(r'^entries/(?P<pk>[0-9]+)/$',views.EntryDetail),
]