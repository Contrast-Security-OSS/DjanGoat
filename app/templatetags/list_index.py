from django import template

register = template.Library()


@register.filter
def index(L, arg):
    return L[arg]
