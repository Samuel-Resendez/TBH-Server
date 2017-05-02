from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from toBeHuman import views


urlpatterns = [
    url(r'^entries/$',views.EntryList.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)/$',views.EntryDetail.as_view())
]