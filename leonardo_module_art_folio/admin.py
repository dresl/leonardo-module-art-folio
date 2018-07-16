
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


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class ImageCategoryInline(admin.TabularInline):
    model = ImageCategory


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'ordering']
    list_filter = ['translations__name']
    search_fields = ['translations__name']
    list_per_page = 50
    inlines = [ProjectTranslation_Inline, ProjectImageInline]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


class ProjectImageAdmin(admin.ModelAdmin):
    inlines = [ProjectImageTranslation_Inline]
    list_display = ["__unicode__", "ordering", "featured"]


class ImageCategoryAdmin(admin.ModelAdmin):
    inlines = [ImageCategoryTranslation_Inline]
    list_display = ["__unicode__", "ordering"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ImageCategory, ImageCategoryAdmin)
