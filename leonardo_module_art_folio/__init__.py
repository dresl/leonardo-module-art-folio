
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
            ('leonardo_module_art_folio.apps.projects', 'List of projects'),
        ]

    public = True


class Config(AppConfig):
    name = 'leonardo_module_art_folio'
    verbose_name = "Art folio"

default = Default()
