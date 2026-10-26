"""Order Service checkout calculation module."""

def calculate_order_total(items: list[dict], discount: float = 0.0) -> float:
    """Calculates order total after discount.
    
    BUG: If discount > total or if item price is negative, negative total is returned.
    """
    if not items:
        return 0.0
    subtotal = sum(item.get("price", 0.0) * item.get("quantity", 1) for item in items)
    return subtotal - discount
