from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms.translations import (TranslatedObjectManager,
                                  TranslatedObjectMixin, Translation)
from django.utils import timezone
from django.core.urlresolvers import reverse

CHOICES_IMAGE_STATUS = (
    ('available', _('Available')),
    ('reserve', _('Reserved')),
    ('copy', _('Make copy')),
)

CHOICES_PRODUCT_STATUS = (
    ('available', _('Available')),
    ('sold_out', _('Sold out')),
)

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
    def get_absolute_url(self):
        from leonardo.module.web.widget.application.reverse import app_reverse
        return app_reverse(
            'art_detail_project',
            'leonardo_module_art_folio.apps.projects',
            kwargs={
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
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True, default='')

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
        verbose_name = _("Image category")
        verbose_name_plural = _("Image categories")


class ImageCategoryTranslation(Translation(ImageCategory)):

    """
    Translated Project Image Category.
    """

    name = models.CharField(
        verbose_name=_("Name"), max_length=255, default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name


class ImageTheme(models.Model, TranslatedObjectMixin):
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
        verbose_name = _("Image theme")
        verbose_name_plural = _("Image themes")


class ImageThemeTranslation(Translation(ImageTheme)):

    """
    Translated Project Image Category.
    """

    name = models.CharField(
        verbose_name=_("Name"), max_length=255, default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name


class ImageColors(models.Model, TranslatedObjectMixin):
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
        verbose_name = _("Image color")
        verbose_name_plural = _("Image colors")


class ImageColorsTranslation(Translation(ImageColors)):

    """
    Translated Project Image Category.
    """

    name = models.CharField(
        verbose_name=_("Name"), max_length=255, default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name


class ImageFormat(models.Model, TranslatedObjectMixin):
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
        verbose_name = _("Image format")
        verbose_name_plural = _("Image formats")


class ImageFormatTranslation(Translation(ImageFormat)):

    """
    Translated Project Image Category.
    """

    name = models.CharField(
        verbose_name=_("Name (eg. 120x120cm)"), max_length=255, default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name


class ImageTechnique(models.Model, TranslatedObjectMixin):
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
        verbose_name = _("Image technique")
        verbose_name_plural = _("Image techniques")


class ImageTechniqueTranslation(Translation(ImageTechnique)):

    """
    Translated Project Image Category.
    """

    name = models.CharField(
        verbose_name=_("Name (eg. 120x120cm)"), max_length=255, default='')

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
    # main attributes
    categories = models.ManyToManyField(
        ImageCategory, verbose_name=_("Categories"), blank=True, null=True)
    theme = models.ManyToManyField(
        ImageTheme, verbose_name=_("Theme"), blank=True, null=True)
    colors = models.ManyToManyField(
        ImageColors, verbose_name=_("Colors"), blank=True, null=True)
    image_format = models.ManyToManyField(
        ImageFormat, verbose_name=_("Format"), blank=True, null=True)
    technique = models.ManyToManyField(
        ImageTechnique, verbose_name=_("Technique"), blank=True, null=True)
    # others
    ordering = models.PositiveIntegerField(
        verbose_name=_("Ordering"), default=0)
    featured = models.BooleanField(
        verbose_name=_("Featured Image"), default=False)
    # status
    status = models.CharField(
        verbose_name=("Status"), default=CHOICES_IMAGE_STATUS[0][0], choices=CHOICES_IMAGE_STATUS, max_length=255)

    pub_date = models.DateTimeField(
        _('Published on'),
        blank=True, null=True, default=timezone.now, db_index=True,
        help_text=_(
            'Will be filled in automatically when picture gets published.'))

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
        verbose_name=_("Name"), max_length=255, default='')
    slug = models.SlugField(_("Slug"), default="")
    description = models.TextField(
        verbose_name=_("Description"), blank=True, null=True, default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name


class ProjectImageOrder(models.Model):

    picture = models.ForeignKey(ProjectImage, verbose_name=_("Picture"), related_name="orderimage")

    name = models.CharField(
        max_length=255, verbose_name=_("Name"), default='')
    telephone = models.CharField(
        verbose_name=_("Telephone"), max_length=100)
    email = models.EmailField(
        verbose_name=_("E-mail"), default='')
    note = models.TextField(
        verbose_name=_("Note"), default='', blank=True)

    pub_date = models.DateTimeField(_('Order date'), auto_now_add=True)

    def __unicode__(self):
        return self.picture.translation.name

    class Meta:
        ordering = ['pub_date', ]
        verbose_name = _('Picture Order')
        verbose_name_plural = _('Picture Orders')


class OtherProduct(models.Model, TranslatedObjectMixin):

    project = models.ForeignKey(
        Project, related_name="products", verbose_name=_("Project"))
    image = models.ImageField(
        verbose_name=_("Product Image"), upload_to="project_images/")
    # main attributes
    number = models.PositiveIntegerField(
        verbose_name=_("Number of products"), default=20, blank=True, null=True)
    categories = models.ManyToManyField(
        ImageCategory, verbose_name=_("Categories"), blank=True, null=True)
    # others
    ordering = models.PositiveIntegerField(
        verbose_name=_("Ordering"), default=0)
    featured = models.BooleanField(
        verbose_name=_("Featured Image"), default=False)
    # status
    status = models.CharField(
        verbose_name=("Status"), default=CHOICES_PRODUCT_STATUS[0][0], choices=CHOICES_PRODUCT_STATUS, max_length=255)

    pub_date = models.DateTimeField(
        _('Published on'),
        blank=True, null=True, default=timezone.now, db_index=True,
        help_text=_(
            'Will be filled in automatically when picture gets published.'))

    objects = TranslatedObjectManager()

    class Meta:
        verbose_name = _("Other product")
        verbose_name_plural = _("Other products")
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


class OtherProductTranslation(Translation(OtherProduct)):

    """
    Translated Other product.
    """

    name = models.CharField(
        verbose_name=_("Name"), max_length=255, default='')
    slug = models.SlugField(_("Slug"), default="")
    description = models.TextField(
        verbose_name=_("Description"), blank=True, null=True, default='')

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    def __unicode__(self):
        return self.name
