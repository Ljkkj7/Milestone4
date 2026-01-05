from marketplace.models import Sneaker

def cart_totals(request):
    """Provide cart count (sum of quantities) and total price for header display."""
    cart = request.session.get('cart', {})
    count = 0
    total = 0.0

    for sneaker_id_str, data in cart.items():
        try:
            qty = int(data.get('quantity', 0))
            sneaker_id = int(sneaker_id_str)
        except (ValueError, TypeError):
            continue

        try:
            sneaker = Sneaker.objects.get(id=sneaker_id)
        except Sneaker.DoesNotExist:
            continue

        count += qty
        try:
            total += float(sneaker.price) * qty
        except Exception:
            continue

    return {'cart': {'count': count, 'total': total}}