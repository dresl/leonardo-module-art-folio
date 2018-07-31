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
from .models import (Project, ProjectImage,
                    ProjectImageOrder, ImageCategory,
                    ImageTheme, ImageColors, ImageFormat)
from .forms import ProjectImageOrderForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import dates
from django.views.generic import DetailView, ListView, RedirectView
import operator
from django.db.models import Q
from django.utils.text import slugify

CHOICES_AVAILABILITY = (
    ('available', _('Available')),
    ('sold_out', _('Not for sale / Sold out')),
)

class ProjectListView(ListView):
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    slug_field = 'translations__slug'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['all_categories'] = ImageCategory.objects.all()
        context['all_themes'] = ImageTheme.objects.all()
        context['all_colors'] = ImageColors.objects.all()
        context['all_formats'] = ImageFormat.objects.all()
        context['all_statuses'] = CHOICES_AVAILABILITY
        return context


class ProjectImageSearchView(ListView):
    template_name = "leonardo_module_art_folio/project_search.html"
    model = ProjectImage
    queryset = ProjectImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectImageSearchView, self).get_context_data(**kwargs)
        picture_list = self.model.objects.all()

        # name
        name = self.request.GET.get('name')
        if name != None:
            picture_list = picture_list.filter(translations__slug__icontains=slugify(name))
            context['get_name'] = name
        else:
            picture_list = picture_list
        
        # category
        categories_id = self.request.GET.getlist('categories')
        if len(categories_id) != 0:
            image_categories = ImageCategory.objects.filter(id__in=categories_id)
            picture_list = picture_list.filter(categories=image_categories).distinct().order_by("categories")
            context['selected_categories'] = image_categories
        else:
            picture_list = picture_list

        # theme
        themes_id = self.request.GET.getlist('themes')
        if len(themes_id) != 0:
            image_themes = ImageTheme.objects.filter(id__in=themes_id)
            picture_list = picture_list.filter(theme=image_themes).distinct().order_by("theme")
            context['selected_themes'] = image_themes
        else:
            picture_list = picture_list

        # color
        colors_id = self.request.GET.getlist('colors')
        if len(colors_id) != 0:
            image_colors = ImageColors.objects.filter(id__in=colors_id)
            picture_list = picture_list.filter(colors=image_colors).distinct().order_by("colors")
            context['selected_colors'] = image_colors
        else:
            picture_list = picture_list

        # format
        formats_id = self.request.GET.getlist('formats')
        if len(formats_id) != 0:
            image_formats = ImageFormat.objects.filter(id__in=formats_id)
            picture_list = picture_list.filter(image_format=image_formats).distinct().order_by("image_format")
            context['selected_formats'] = image_formats
        else:
            picture_list = picture_list

        # format
        status_id = self.request.GET.getlist('status')
        if len(status_id) != 0:
            if "available" in status_id:
                status_id.append("copy")
            picture_list = picture_list.filter(status__in=status_id).distinct().order_by("status")
            context['selected_status'] = status_id
        else:
            picture_list = picture_list

        context['all_categories'] = ImageCategory.objects.all()
        context['all_themes'] = ImageTheme.objects.all()
        context['all_colors'] = ImageColors.objects.all()
        context['all_formats'] = ImageFormat.objects.all()
        context['all_statuses'] = CHOICES_AVAILABILITY
        context['count_pictures'] = _("%s of %s") % (picture_list.count(), ProjectImage.objects.count())
        context['picture_list'] = picture_list
        context['projects'] = Project.objects.all()
        return context


class ProjectImageOrderCreate(forms.ModalFormView):
    form_class = ProjectImageOrderForm
    template_name = "leonardo_module_art_folio/orderimage_form.html"
    submit_label = "Rezervovat"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(ProjectImageOrderCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['orderimage'] = ProjectImageOrderForm(self.request.POST)
        else:
            context['orderimage'] = ProjectImageOrderForm()
        picture_pk = self.kwargs.get('pk')

        if self.kwargs.get('copy'):
            copy_view = True
        else:
            copy_view = False

        context.update({
            "view_name": "Objednávací formulář",
            "modal_size": 'md',
            "modal_header": 'Objednávací formulář',
            "copy_view": copy_view,
            "picture": ProjectImage.objects.get(pk=picture_pk)
            })
        return context

    def get_initial(self):
        return {'picture': self.kwargs.get('pk')}
