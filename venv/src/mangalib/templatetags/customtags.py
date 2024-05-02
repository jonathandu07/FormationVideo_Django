from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def first_char(value):
    return value[0]


# Il est possible de renommer une fonction en utilisant un décorateur :
@register.filter(name = "longueur_de_ça")
def checkstrlen(value, size):
    return len(value) == size