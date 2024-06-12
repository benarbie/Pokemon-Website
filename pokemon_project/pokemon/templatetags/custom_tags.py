from django import template

register = template.Library()

@register.filter
def get_element(list, i):
    return list[i]

@register.filter
def divide_and_multiply(value1, value2):
    try:
        return value1 / value2 * 100
    except(ValueError, ZeroDivisionError):
        return None

@register.filter
def calculate_color(stat):
    
    if 0 <=  stat < 25:
        return '#e24a4ae8'
    if 25 <= stat < 50:
        return '#ee7613ef'
    if 50 <= stat < 100:
        return '#ffd43b'
    if 100 <= stat < 120:
        return '#69db7c'
    if 120 <= stat < 150:
        return '#12b85d'
    if 150 <= stat:
        return '#15aabf'
