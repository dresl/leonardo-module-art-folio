from django.conf.urls import url
from leonardo_module_art_folio.views import (ProjectListView,
                                            ProjectDetailView)


def artfolio_patterns(list_kwargs={}, detail_kwargs={}):
    return [
        url(r'^$',
            ProjectListView.as_view(**list_kwargs), name='art_list_project'),
        url(r'^(?P<slug>[\w-]+)/$',
            ProjectDetailView.as_view(**detail_kwargs), name='art_detail_project'),
    ]


urlpatterns = artfolio_patterns()
