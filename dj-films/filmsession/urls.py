from django.conf.urls import url


from .views import (
    SessionCreateView,
    SessionDetailView,
    SessionListView,
    SessionUpdateView,
)
urlpatterns = [
    url(r'^create/$',  SessionCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', SessionUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', SessionUpdateView.as_view(), name='detail'),
    url(r'$', SessionListView.as_view(), name='list'),
]
