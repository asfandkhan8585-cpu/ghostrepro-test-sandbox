import pytest
from order_service import calculate_order_total

def test_empty_cart():
    assert calculate_order_total([]) == 0.0

def test_standard_order():
    items = [{"price": 100.0, "quantity": 2}, {"price": 50.0, "quantity": 1}]
    assert calculate_order_total(items, discount=20.0) == 230.0
