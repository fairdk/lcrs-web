from __future__ import absolute_import, unicode_literals

from django import template
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import BaseForm
from django.forms.fields import BooleanField
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.inclusion_tag('konsensus/bootstrap/form.html', takes_context=True)
def bootstrap_form(context, form_obj, skip_fields=False):
    # Do not reuse the context as concurrency apparently means that when you
    # use multiple inclusion tags on the same page, one overwrites the other's
    # context
    # context = RequestContext(context['request'])
    if not isinstance(form_obj, BaseForm):
        raise TypeError(
            "Error including form, it's not a form, it's a %s" %
            type(form_obj))
    context['bootstrap_form'] = form_obj
    context['skip_fields'] = skip_fields
    return context


@register.filter()
def bootstrap_render_field(field, extra_class=''):

    return field.as_widget(attrs={'class': 'form-control ' + extra_class})


@register.filter()
def is_checkbox(field):
    return isinstance(field.field, BooleanField)


@register.inclusion_tag('konsensus/bootstrap/button_panel.html', takes_context=True)
def bootstrap_buttons(context, submit=_("Submit"), submit2_label=None, submit2_name=None, go_back=None, reset=False):

    if go_back is not None:
        referer = getattr(context.get('request', {}), 'META', {}).get(
            'HTTP_REFERER', None)
        if not referer:
            referer = reverse('login')
        go_back = {
            'label': go_back,
            'referer': referer
        }

    submit2 = None
    if submit2_label is not None:
        submit2 = {
            'label': submit2_label,
            'name': submit2_name,
        }

    context.update({
        'button_submit': submit,
        'go_back': go_back,
        'reset': reset,
        'submit2': submit2,
    })
    return context


@register.filter()
def bootstrap_message_tag(message):
    """Takes a message object from django.contrib.message and returns
    a bootstrap danger/warning/info/success/default CSS class"""
    lvl = message.level
    if lvl >= messages.ERROR:
        return 'danger'
    if lvl >= messages.WARNING:
        return 'warning'
    if lvl >= messages.SUCCESS:
        return 'success'
    if lvl >= messages.INFO:
        return 'info'
    return 'default'
