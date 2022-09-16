from decimal import Decimal
from django.conf import settings
from category.models import Products
from home.models import Claim


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Products.objects.filter(id__in=product_ids)
        

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """

        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def decrease(self, product):
        """
        Decrease item count
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= 1
            if self.cart[product_id]['quantity'] <= 0:
                self.remove(product)
            self.save()


    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        deals = Claim.objects.all()
        for item in self.cart.values():
            for deal in deals:
                if len(deal.products.filter(id = item["product"].id )) != 0:
                    if deal.deal_choices == "percent":
                        item['price'] = int(Decimal(item['price']) - Decimal((deal.deal_sum/100)) * Decimal(item['price']))
                    else:
                        item['price'] = int(item["price"] - deal.deal_sum)
                else:
                    item['price'] = Decimal(item['price'])
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def cart_products(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids).values_list()
        return len(products)