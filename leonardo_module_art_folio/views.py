# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.utils.translation import get_language

from django import forms as django_forms
from leonardo import forms, messages
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
from .models import Project, ProjectImage, ProjectImageOrder
from .forms import ProjectImageOrderForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import dates
from django.views.generic import DetailView, ListView, RedirectView
import operator
from django.db.models import Q


class ProjectListView(ListView):
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    slug_field = 'translations__slug'

    def get_context_data(self, **kwargs):
      context = super(ProjectDetailView, self).get_context_data(**kwargs)
      context['projects'] = Project.objects.all()
      return context


class ProjectSearchView(ListView):
    template_name = "leonardo_module_art_folio/project_search.html"
    model = ProjectImage
    paginate_by = 5
    queryset = ProjectImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectSearchView, self).get_context_data(**kwargs)
        
        try:
          name = self.request.GET.get('q')
        except:
          name = ''
        
        if name == None:
          name = ""

        list_picture = self.model.objects.filter(translations__name__icontains=name)

        paginator = Paginator(list_picture, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            pictures = paginator.page(page)
        except PageNotAnInteger:
            pictures = paginator.page(1)
        except EmptyPage:
            pictures = paginator.page(paginator.num_pages)

        context['picture_list'] = pictures
        return context


class ProjectImageOrderCreate(forms.ModalFormView):
    form_class = ProjectImageOrderForm
    template_name = "leonardo_module_art_folio/orderimage_form.html"
    submit_label = "Objednat"
    success_url = "/"

    def get_context_data(self, **kwargs):
        ret = super(ProjectImageOrderCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            ret['orderimage'] = ProjectImageOrderForm(self.request.POST)
        else:
            ret['orderimage'] = ProjectImageOrderForm()
        picture_pk = self.kwargs.get('pk')

        ret.update({
            "view_name": "Objednávací formulář",
            "modal_size": 'md',
            "modal_header": 'Objednávací formulář',
            "picture": ProjectImage.objects.get(pk=picture_pk)
            })
        return ret

    def get_initial(self):
        return {'picture': self.kwargs.get('pk')}
