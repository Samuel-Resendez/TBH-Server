from django.conf.urls import url
from TBHServer import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$',views.EntryList.as_view()),
    url(r'^entries/$',views.EntryList.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)/$',views.EntryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)