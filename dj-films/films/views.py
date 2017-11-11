from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import FilmadCreateForm, FilmCreateForm
from .models import Film


class FilmadListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Film.objects.filter(owner=self.request.user)


class FilmadDetailView(LoginRequiredMixin, DetailView):
     def get_queryset(self):
        return Film.objects.filter(owner=self.request.user)

class FilmadCreateView(LoginRequiredMixin, CreateView):
    form_class = FilmCreateForm
    login_url = '/login/'
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(FilmadCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(FilmadCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Film'
        return context


class FilmadUpdateView(LoginRequiredMixin, UpdateView):
    form_class = FilmCreateForm
    login_url = '/login/'
    template_name = 'films/detail-update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FilmadUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update Film: {name}'
        return context

    def get_queryset(self):
        return Film.objects.filter(owner=self.request.user)



        






