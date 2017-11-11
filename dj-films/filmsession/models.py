from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from films.models import Film

class Session(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    film            = models.ForeignKey(Film)
    public          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def get_absolute_url(self): 
        return reverse('filmsession:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']
