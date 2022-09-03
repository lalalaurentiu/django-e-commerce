from django import template
  
register = template.Library()

@register.filter(name="times")
def range_iterator(value):
    return range(1, value)

@register.filter(name="len")
def query_len(query):
    return len(query)

@register.filter(name="cartlen")
def cart_len(cart):
    print(len(cart))
    return len(cart)
