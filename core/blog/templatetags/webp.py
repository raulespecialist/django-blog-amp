import os
from django import template

register = template.Library()

@register.filter
def webp(string):
    path_webp = str(os.path.splitext(string)[0] + '.webp')
    return(path_webp)