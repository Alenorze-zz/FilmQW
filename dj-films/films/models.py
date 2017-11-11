from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

from filmgenre.models import Genre

User = settings.AUTH_USER_MODEL



class FilmQuerySet(models.query.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(location__iexact=query)|
                Q(category__icontains=query)|
                Q(category__iexact=query)|
                Q(item__name__icontains=query)|
                Q(item__contents__icontains=query)
                ).distinct()
        return self


class Film(models.Model):
    owner           = models.ForeignKey(User)
    name            = models.CharField(max_length=120)
    description     = models.CharField(max_length=2000)
    poster          = models.ImageField()
    genre           = models.ForeignKey(Genre)
    premiere        = models.DateField()
    sessiontime     = models.DateTimeField()
    durability      = models.IntegerField()
    price           = models.IntegerField()
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('films:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Film)





