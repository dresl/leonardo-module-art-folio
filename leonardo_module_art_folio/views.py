from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.utils.translation import get_language

from django import forms
from django.conf import settings
from django.contrib.admin import widgets
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)
from django.template import RequestContext
from django.utils.encoding import uri_to_iri
from django.utils.translation import ugettext_lazy as _
from constance import config
from .models import Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import dates
from django.views.generic import DetailView, ListView, RedirectView


class ProjectListView(ListView):
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    slug_field = 'translations__slug'

    def get_context_data(self, **kwargs):
      context = super(ProjectDetailView, self).get_context_data(**kwargs)
      context['projects'] = Project.objects.all()
      return context
