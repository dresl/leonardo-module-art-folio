
from django.contrib import admin
from django.db import models
from .models import (Project,
                     ProjectTranslation,
                     ProjectImage,
                     ProjectImageTranslation,
                     ImageCategory,
                     ImageCategoryTranslation,
                     ImageTheme,
                     ImageThemeTranslation,
                     ImageColors,
                     ImageColorsTranslation,
                     ImageFormat,
                     ImageFormatTranslation,
                     ImageTechnique,
                     ImageTechniqueTranslation,
                     ProjectImageOrder
                    )

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

ProjectImageTranslation_Inline = admin_translationinline(
    ProjectImageTranslation,
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

ImageThemeTranslation_Inline = admin_translationinline(
    ImageThemeTranslation,
    formfield_overrides={
        models.TextField: {'widget': CKEditorWidget}
    })

ImageColorsTranslation_Inline = admin_translationinline(
    ImageColorsTranslation,
    formfield_overrides={
        models.TextField: {'widget': CKEditorWidget}
    })

ImageFormatTranslation_Inline = admin_translationinline(
    ImageFormatTranslation,
    formfield_overrides={
        models.TextField: {'widget': CKEditorWidget}
    })

ImageTechniqueTranslation_Inline = admin_translationinline(
    ImageTechniqueTranslation,
    formfield_overrides={
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
    fields = ["get_edit_link", "image", "categories",
              "theme", "image_format", "colors",
              "technique", "status", "ordering", "featured", thumb]
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
    list_display = ["__unicode__", thumb, "status", "ordering", "pub_date", "featured"]
    list_editable = ["status", "ordering", "featured"]
    list_filter = ["image_format", "colors", "theme", "categories", "project"]
    search_fields = ['translations__name']
    fields = ["project", "image", "categories", "theme",
              "image_format", "colors", "technique",
               "status", "ordering", "pub_date", "featured", thumb_large]
    readonly_fields = [thumb_large]


class ImageCategoryAdmin(admin.ModelAdmin):
    inlines = [ImageCategoryTranslation_Inline]
    list_display = ["__unicode__", "ordering"]

class ImageThemeAdmin(admin.ModelAdmin):
    inlines = [ImageThemeTranslation_Inline]
    list_display = ["__unicode__", "ordering"]

class ImageColorsAdmin(admin.ModelAdmin):
    inlines = [ImageColorsTranslation_Inline]
    list_display = ["__unicode__", "ordering"]

class ImageFormatAdmin(admin.ModelAdmin):
    inlines = [ImageFormatTranslation_Inline]
    list_display = ["__unicode__", "ordering"]

class ImageTechniqueAdmin(admin.ModelAdmin):
    inlines = [ImageTechniqueTranslation_Inline]
    list_display = ["__unicode__", "ordering"]


class ProjectImageOrderAdmin(admin.ModelAdmin):
    model = ProjectImageOrder
    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['pub_date']
        else:
            return ['pub_date']
        return []
    list_display = ('picture', 'name', 'telephone', 'email', 'note', 'pub_date')
    list_filter = ['pub_date','name']
    search_fields = ['name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ImageCategory, ImageCategoryAdmin)
admin.site.register(ImageTheme, ImageThemeAdmin)
admin.site.register(ImageColors, ImageColorsAdmin)
admin.site.register(ImageFormat, ImageFormatAdmin)
admin.site.register(ImageTechnique, ImageTechniqueAdmin)
admin.site.register(ProjectImageOrder, ProjectImageOrderAdmin)
