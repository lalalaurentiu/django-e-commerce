from unittest import result
from django import template
  
register = template.Library()

@register.filter(name="times")
def range_iterator(value):
    return range(1, value)
