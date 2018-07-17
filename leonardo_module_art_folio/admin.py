
from django.contrib import admin
from django.db import models
from .models import (Project,
                     ProjectTranslation,
                     ImageCategory,
                     ImageCategoryTranslation,
                     ProjectImage,
                     ProjectImageTranslation,)

from feincms.translations import admin_translationinline
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext as _
from sorl.thumbnail import get_thumbnail
from django.core.urlresolvers import reverse
from django.utils.text import force_text


ProjectTranslation_Inline = admin_translationinline(
    ProjectTranslation,
    prepopulated_fields={
        'slug': ('name',)
    }, formfield_overrides={
        models.TextField: {'widget': CKEditorWidget}
    })

ImageCategoryTranslation_Inline = admin_translationinline(
    ImageCategoryTranslation,
    formfield_overrides={
        models.TextField: {'widget': CKEditorWidget}
    })

ProjectImageTranslation_Inline = admin_translationinline(
    ProjectImageTranslation, formfield_overrides={
        models.TextField: {'widget': CKEditorWidget}
    })


def thumb(object):
    if object.image:
        thumb = get_thumbnail(object.image, "x150", format='PNG')
        return "<img src='%s' alt='' />" % thumb.url
    else:
        return 'N/A'
thumb.short_description = _('Preview')
thumb.allow_tags = True

def thumb_large(object):
    if object.image:
        thumb_large = get_thumbnail(object.image, "x250", format='PNG')
        return "<img src='%s' alt='' />" % thumb_large.url
    else:
        return 'N/A'
thumb_large.short_description = _('Preview')
thumb_large.allow_tags = True


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 0
    fields = ["get_edit_link", "image", "categories", "ordering", "featured", thumb]
    readonly_fields = ["get_edit_link", thumb]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            )
        return _("(save and continue editing to create a link)")
    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True


class ImageCategoryInline(admin.StackedInline):
    model = ImageCategory
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'ordering']
    search_fields = ['translations__name']
    list_editable = ['ordering']
    list_per_page = 50
    inlines = [ProjectTranslation_Inline, ProjectImageInline]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


class ProjectImageAdmin(admin.ModelAdmin):
    inlines = [ProjectImageTranslation_Inline]
    list_display = ["__unicode__", thumb, "ordering", "featured"]
    list_editable = ["ordering", "featured"]
    list_filter = ["project", "categories"]
    search_fields = ['translations__name']
    fields = ["image", "categories", "ordering", "featured", thumb_large]
    readonly_fields = [thumb_large]


class ImageCategoryAdmin(admin.ModelAdmin):
    inlines = [ImageCategoryTranslation_Inline]
    list_display = ["__unicode__", "ordering"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ImageCategory, ImageCategoryAdmin)
