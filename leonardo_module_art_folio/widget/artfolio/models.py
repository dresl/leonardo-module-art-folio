# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Page, Widget
from leonardo_module_art_folio.models import Project


class ArtFolioWidget(Widget):

    project = models.ForeignKey(Project, verbose_name='Project')

    class Meta:
        abstract = True
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
