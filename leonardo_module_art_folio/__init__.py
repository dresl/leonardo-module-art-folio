# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_module_art_folio.Config'


class Default(object):
    optgroup = 'Art folio'

    @property
    def apps(self):
        return [
            'leonardo_module_art_folio',

        ]

    @property
    def widgets(self):
        return [
            'leonardo_module_art_folio.widget.artfolio.models.ArtFolioWidget',
        ]

    @property
    def plugins(self):
        return [
            ('leonardo_module_art_folio.apps.projects', 'Art folio projects'),
        ]

    @property
    def css_files(self):
        return [
            'css/slick.css',
            'css/slick-theme.css',
        ]
    
    @property
    def js_files(self):
        return [
            'js/slick.min.js'
        ]

    config = {
        'ORDER_DEFAULT_TO_EMAIL':
        ('to@email.com', u"E-mail, na který se budou odesílat objednávky."),
    }

    ordering = -3

    public = True


class Config(AppConfig):
    name = 'leonardo_module_art_folio'
    verbose_name = "Art folio"

default = Default()
