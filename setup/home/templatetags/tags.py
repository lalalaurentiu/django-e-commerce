from django import template
from ..models import Claim
  
register = template.Library()

@register.filter(name="times")
def range_iterator(value):
    return range(1, value)

@register.filter(name="len")
def query_len(query):
    return len(query)

@register.filter(name="cartlen")
def cart_len(cart):
    return len(cart)

@register.filter(name="totalPrice")
def total_price(obj):
    print(obj)
    total = 0
    for item in obj:
        total += item["price"]

    return total

@register.filter(name="deals")
def deal_product(price, value):
    if value.deal_choices == "percent":
        return int(float(price) - ((value.deal_sum/100)*float(price)))
    else:
        return int(float(price) - value.deal_sum)
