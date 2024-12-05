import pytest
pytest.main(["--junitxml=report.xml"])
from lab import (
    product, quotient, euclidean_distance, solve_quadratic_equation, 
    sum_geometric_series
)

#Тимофеева ЭА107б2

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2), (-3, 4, -12), (0, 100, 0), (-7, -6, 42), (0, 0, 0)
])
def test_product(a, b, expected):
    assert product(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3), (10, 5, 2), (1, 0, None), (100, 25, 4), (10, 3, 10 / 3)
])
def test_quotient(a, b, expected):
    assert quotient(a, b) == expected


@pytest.mark.parametrize("x1, y1, x2, y2, expected", [
    (0, 0, 0, 0, 0), (1, 1, 4, 5, 5), (-2, -2, 3, 3, 7.0710678118654755),
    (0, 0, 10, 0, 10), (1, 2, 3, 2, 2)
])
def test_euclidean_distance(x1, y1, x2, y2, expected):
    assert euclidean_distance(x1, y1, x2, y2) == expected

@pytest.mark.parametrize("a, b, c, expected", [
    (1, -3, 2, (2, 1)), (1, -2, 1, 1), (1, 2, 1, -1),
    (1, 4, 5, None), (1, 0, -4, (2, -2))
])
def test_solve_quadratic_equation(a, b, c, expected):
    assert solve_quadratic_equation(a, b, c) == expected

#Тимофеева ЭА107б2

@pytest.mark.parametrize("a, r, n, expected", [
    (1, 2, 3, 7), (3, 1, 4, 12), (5, 0.5, 5, 9.6875), 
    (2, 0.5, 6, 3.9375), (10, 3, 2, 40)
])
def test_sum_geometric_series(a, r, n, expected):
    assert sum_geometric_series(a, r, n) == expected

