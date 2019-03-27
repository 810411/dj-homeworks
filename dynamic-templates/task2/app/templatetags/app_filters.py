from django import template

register = template.Library()


@register.filter
def active(path, href):
    return 'active' if path.strip('/') == href else ''
