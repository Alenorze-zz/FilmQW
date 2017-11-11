from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


from django.contrib.auth.views import LoginView, LogoutView

from filmsession.views import HomeView, AllUserRecentItemListView
from profiles.views import RegisterView, activate_user_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^sessions/', include('filmsession.urls', namespace='filmsession')),
    url(r'^films/', include('films.urls', namespace='films')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
