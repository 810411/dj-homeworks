from django import template

register = template.Library()


@register.filter(name='color')
def color_class(value):
    num = float(value or 0)

    if num < 0:
        return 'green'
    elif 1 < num <= 2:
        return 'red lighten-5'
    elif 2 < num <= 5:
        return 'red lighten-3'
    elif num > 5:
        return 'red'

    return ''
