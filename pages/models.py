from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from . import fields


class LCRSPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('three_columns', fields.ThreeColumnsBlock()),
    ], default="")

    content_panels = Page.content_panels + [  # @UndefinedVariable
        StreamFieldPanel('body'),
    ]


class MailingListSignup(models.Model):
    
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
