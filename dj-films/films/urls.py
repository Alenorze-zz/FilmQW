from django.conf.urls import url


from .views import (
    FilmadListView,
    FilmadDetailView,
    FilmadCreateView,
    FilmadUpdateView

)
urlpatterns = [
    url(r'^create/$',  FilmadCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', FilmadUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', FilmadUpdateView.as_view(), name='detail'),
    url(r'$', FilmadListView.as_view(), name='list'),
]
