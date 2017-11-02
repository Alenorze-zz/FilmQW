from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
