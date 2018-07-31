# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.utils import timezone

from crispy_forms.layout import \
    HTML, Field, Layout, Fieldset, MultiField, Div, Submit, ButtonHolder
from crispy_forms.bootstrap import PrependedText
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import \
    default_token_generator as token_generator
from django import forms as django_forms
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from horizon.utils import validators
from horizon_contrib.forms import SelfHandlingModelForm, SelfHandlingForm
from django.forms import inlineformset_factory
from django.db import models
from django.forms import Field as DjangoField
from .models import ProjectImage, ProjectImageOrder
from django.conf import settings
from horizon import forms, messages
from leonardo.utils.emails import send_templated_email as send_mail


CHOICES_STATUS = (
    ('sold_out', _('Reserve')),
    ('copy', _('Order copy')),
)

class ProjectImageOrderForm(SelfHandlingForm):

    import sys
    reload(sys)
    sys.setdefaultencoding('UTF8')

    error_required = _('This field is required.')
    invalid_email_message = _('Make sure you have correct e-mail format.')

    picture = forms.CharField(label="Picture",
                            max_length=255,
                            widget=forms.HiddenInput(),
                            error_messages={'required': error_required})

    name = forms.CharField(label=_('Name'),
                            max_length=255,
                            widget=forms.TextInput(
                                attrs={'placeholder':
                                       _('Name'),
                                       'autofocus': 'autofocus'}),
                            error_messages={'required': error_required})

    telephone = forms.CharField(label=_('Telephone'),
                            max_length=255,
                            widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Telephone')}),
                            error_messages={'required': error_required})

    email = forms.EmailField(label='E-mail',
                            widget=forms.EmailInput(
                                 attrs={'placeholder': 'E-mail'}),
                            error_messages={'required': error_required,
                                             'invalid': invalid_email_message})

    note = forms.CharField(label=_('Note'),
                            widget=forms.Textarea(
                                     attrs={'placeholder': _('Any note?')}),
                            required=False)

    status = forms.ChoiceField(label = _('I want to'),
                            widget=forms.RadioSelect(),
                            choices=CHOICES_STATUS,
                            error_messages={'required': error_required})

    def __init__(self, *args, **kwargs):
        super(ProjectImageOrderForm, self).__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Div('picture', style='padding:5px', css_class='col-md-12'),
            Div('name', style='padding:5px', css_class='col-md-6'),
            Div('telephone', style='padding:5px', css_class='col-md-6'),
            PrependedText('email', '@', placeholder="E-mail"),
            Div('note', 'status', style='padding:5px',
                css_class='col-md-12'),
        )

    def handle(self, request, data):
        project_image = ProjectImage.objects.get(id=int(data['picture']))
        if data['status'] == 'sold_out':
            project_image.status = data['status']
        project_image.save()
        picture_order = ProjectImageOrder.objects.create(
            picture=project_image,
            name=data['name'],
            telephone=data['telephone'],
            email=data['email'],
            note=data['note'],
            pub_date=timezone.now(),
            status=data['status'],
        )
        picture_order.save()
        # send mail
        subject_order = "Objednávka - " + picture_order.name
        send_mail(
            subject_order,
            'leonardo_module_art_folio/orderimage_email.html', {
                'order_title': "Objednávka",
                'order': picture_order,
                'domain': request.site.domain,
            },
            [email.strip() for email in settings.ORDER_DEFAULT_TO_EMAIL.split(',')],
            fail_silently=False,
        )
        # send confirmation
        send_mail(
            'Potvrzení o objednávce obrazu',
            'leonardo_module_art_folio/orderimage_email.html', {
                'order_title': "Potvrzení o objednávce",
                'order': picture_order,
            },
            picture_order.email,
            fail_silently=False,
        )
        messages.success(request,
            "Objednávka úspěšně dokončena. Název obrazu: %s" % project_image.translation.name)
        return True
