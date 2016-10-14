from django import template
register = template.Library()

from wagtail.wagtailcore.models import Page

# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.assignment_tag(takes_context=True)
def get_menu(context, page=None):
    root_page = Page.objects.get(depth=2)  # @UndefinedVariable
    children = root_page.get_children().filter(
        live=True,
    )
    return children
