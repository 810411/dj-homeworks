from django import template

register = template.Library()


@register.filter(name='crossout')
def cross_out_blank(value):
    return value if value else '-'


@register.filter(name='color')
def color_class(value):
    try:
        num = float(value)
        if num < 0:
            return 'green'
        elif 1 < num <= 2:
            return 'red lighten-5'
        elif 2 < num <= 5:
            return 'red lighten-3'
        elif num > 5:
            return 'red'
    except ValueError as e:
        print(e)

    return ''
