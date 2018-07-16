from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms.translations import (TranslatedObjectManager,
                                  TranslatedObjectMixin, Translation)
from django.core.urlresolvers import reverse
from leonardo.module.media.models.foldermodels import Folder
from leonardo.module.media.models.media import Video
from leonardo.module.media.models.imagemodels import Image
from leonardo.module.media.models.filemodels import File


class Project(models.Model, TranslatedObjectMixin):
    ordering = models.PositiveIntegerField(
        verbose_name=_("Ordering"), default=0)

    objects = TranslatedObjectManager()

    def __unicode__(self):
        trans = None

        # This might be provided using a .extra() clause to avoid hundreds of
        # extra queries:
        if hasattr(self, "preferred_translation"):
            trans = getattr(self, "preferred_translation", u"")
        else:
            try:
                trans = unicode(self.translation)
            except models.ObjectDoesNotExist:
                pass
            except AttributeError:
                pass

        if trans:
            return trans
        else:
            return str(self.ordering)

    @property
    def primary_image(self):
        return self.images.filter(featured=True).first()

    @property
    def files(self):
        try:
            files = File.objects.filter(folder_id=self.folder.id)
        except:
            files = []
        return files

    def get_absolute_url(self):
        from leonardo.module.web.widget.application.reverse import app_reverse
        return app_reverse(
            'detail_project',
            'leonardo_module_art_folio.apps.projects',
            kwargs={
                'category_slug': self.category.translation.slug,
                'slug': self.translation.slug})

    class Meta:
        ordering = ['ordering']
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class ProjectTranslation(Translation(Project)):

    """
    Translated project.
    """

    name = models.CharField(
        max_length=255, verbose_name=_("Name"), default='')
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(verbose_name=_("Description"), default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name

class ImageCategory(models.Model, TranslatedObjectMixin):
    ordering = models.PositiveIntegerField(
        verbose_name=_("Ordering"), default=0)

    objects = TranslatedObjectManager()

    def __unicode__(self):
        trans = None

        # This might be provided using a .extra() clause to avoid hundreds of
        # extra queries:
        if hasattr(self, "preferred_translation"):
            trans = getattr(self, "preferred_translation", u"")
        else:
            try:
                trans = unicode(self.translation)
            except models.ObjectDoesNotExist:
                pass
            except AttributeError:
                pass

        if trans:
            return trans
        else:
            return str(self.ordering)

    class Meta:
        ordering = ["ordering"]
        verbose_name = _("Project category")
        verbose_name_plural = _("Project categories")


class ImageCategoryTranslation(Translation(ImageCategory)):

    """
    Translated Project Image Category.
    """

    name = models.CharField(
        verbose_name=_("Name"), default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name


class ProjectImage(models.Model, TranslatedObjectMixin):
    project = models.ForeignKey(
        Project, related_name="images", verbose_name=_("Project"))
    image = models.ImageField(
        verbose_name=_("Project Image"), upload_to="project_images/")
    categories = models.ManyToManyField(
        ProjectImageCategory, verbose_name="Categories")
    ordering = models.PositiveIntegerField(
        verbose_name=_("Ordering"), default=0)
    featured = models.BooleanField(
        verbose_name=_("Featured Image"), default=False)

    objects = TranslatedObjectManager()

    class Meta:
        verbose_name = _("Project Image")
        verbose_name_plural = _("Project Images")
        ordering = ['ordering']

    def __unicode__(self):
        trans = None

        # This might be provided using a .extra() clause to avoid hundreds of
        # extra queries:
        if hasattr(self, "preferred_translation"):
            trans = getattr(self, "preferred_translation", u"")
        else:
            try:
                trans = unicode(self.translation)
            except models.ObjectDoesNotExist:
                pass
            except AttributeError:
                pass

        if trans:
            return trans
        else:
            return str(self.ordering)


class ProjectImageTranslation(Translation(ProjectImage)):

    """
    Translated Project Image.
    """

    name = models.CharField(
        verbose_name=_("Name"), default='')
    description = models.TextField(
        verbose_name=_("Description"), default='')
    size = models.CharField(
        verbose_name=_("Size"), default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name
