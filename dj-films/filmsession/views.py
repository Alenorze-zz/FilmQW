from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from .forms import SessionForm
from .models import Session

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            object_list = Session.objects.filter(public=True).order_by('-timestamp')
            return render(request, "home.html", {"object_list": object_list})
        return render(request, "filmsession/home-feed.html")


class AllUserRecentItemListView(ListView):
    template_name = 'home.html'
    def get_queryset(self):
        return Session.objects.filter(user__is_active=True)


class SessionListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)


class SessionDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)


class SessionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = SessionForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(SessionCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(SessionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(SessionCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Item'
        return context


class SessionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'filmsession/detail-update.html'
    form_class = SessionForm

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(SessionUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context

    def get_form_kwargs(self):
        kwargs = super(SessionUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

