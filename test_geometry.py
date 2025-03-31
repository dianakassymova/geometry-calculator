import pytest
from geometry import calculate_area

def test_calculate_area():
    """Тест для функции calculate_area."""
    assert calculate_area(1) == pytest.approx(3.14159, rel=1e-5)
    assert calculate_area(0) == 0
    assert calculate_area(2) == pytest.approx(12.56637, rel=1e-5)