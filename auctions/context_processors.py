def cart_context(request):
    
    if request.user.is_authenticated:
        from auctions.models import Listing
        cart = Listing.objects.filter(cart_items__user=request.user)
        cart_count = cart.count()
    else:
        cart = []
        cart_count = 0
    
    return {
        'cart': cart,
        'cart_count': cart_count
    }