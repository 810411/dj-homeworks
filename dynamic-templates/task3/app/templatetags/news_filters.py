from datetime import datetime

from django import template

register = template.Library()


def decl_of_num(num, titles):
    """Функция склонения описания количества
        Аргументы:
        num -- численное представление количества
        titles -- список вариантов склонения описания количества
    """
    cases = [2, 0, 1, 1, 1, 2]

    if 4 < num % 100 < 20:
        index = 2
    elif num % 10 < 5:
        index = cases[num % 10]
    else:
        index = 5

    return titles[index]


@register.filter
def format_date(value):
    # Ваш код
    sec_in_minute = 60
    sec_in_hour = 60 * sec_in_minute

    datetime_now = datetime.now()
    datetime_publication = datetime.fromtimestamp(value)
    delta = datetime_now - datetime_publication

    delta_seconds = delta.total_seconds()
    delta_minutes = delta_seconds // sec_in_minute
    delta_hours = int(delta_seconds // sec_in_hour)

    if delta_minutes < 10:
        return 'только что'
    elif delta_hours < 24:
        return f'{delta_hours} {decl_of_num(delta_hours, ["час", "часа", "часов"])} назад'

    return datetime_publication


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value, default):
    if int(value):
        if value < -5:
            return 'все плохо'
        elif value > 5:
            return 'хорошо'

        return 'нейтрально'

    return default


@register.filter
def format_num_comments(value):
    # Ваш код
    if value == 0:
        return 'Оставьте комментарий'
    elif value > 50:
        return '50+'

    return value


@register.filter
def format_selftext(value, count):
    selftext_words = value.split()

    if len(selftext_words) > count * 2 + 1:
        return '{} ... {}'.format(" ".join(selftext_words[0: count]), " ".join(selftext_words[-count:]))

    return value
