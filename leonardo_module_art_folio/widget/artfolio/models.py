# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Page, Widget, ListWidget
from leonardo_module_art_folio.models import (Project, ProjectImage,
                    ProjectImageOrder, ImageCategory,
                    ImageTheme, ImageColors, ImageFormat)
from leonardo_module_art_folio.views import CHOICES_AVAILABILITY

class ArtFolioWidget(ListWidget):

    picture_count = models.IntegerField("Picture count", blank=True, null=True)
    featured = models.BooleanField("Featured only", default=False, blank=True)
    project = models.ForeignKey(Project, verbose_name="Project", blank=True, null=True)

    def get_items(self):
        pictures = ProjectImage.objects.all().order_by("-pub_date")
        if self.featured:
            pictures = pictures.filter(featured=True)
        if self.project:
            pictures = pictures.filter(project=self.project)
        if pictures.count() > self.picture_count:
            return pictures[:self.picture_count]
        else:
            return pictures

    def get_image_categories(self):
        return ImageCategory.objects.all()

    def get_image_themes(self):
        return ImageTheme.objects.all()

    def get_image_colors(self):
        return ImageColors.objects.all()

    def get_image_formats(self):
        return ImageFormat.objects.all()

    def get_image_statuses(self):
        return CHOICES_AVAILABILITY

    class Meta:
        abstract = True
        verbose_name = _("Art folio")
        verbose_name_plural = _("Art folios")
