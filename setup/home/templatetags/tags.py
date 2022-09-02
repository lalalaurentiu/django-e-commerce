from django import template
  
register = template.Library()

@register.filter(name="times")
def range_iterator(value):
    return range(1, value)

@register.filter(name="len")
def query_len(query):
    print(query)
    return len(query)