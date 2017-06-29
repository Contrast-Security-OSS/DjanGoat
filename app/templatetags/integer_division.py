from django import template

register = template.Library()


@register.filter
def integer_division(value, arg):
    return value/arg
