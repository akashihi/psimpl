import pytest

from psimpl import distancer, simplify, validate_segment


@pytest.mark.parametrize(
    "a,b,c,distance",
    [
        ((0, 0), (0, 10), (5, 5), 5),
        ((0, 0), (10, 0), (5, 5), 5),
        ((0, 0), (10, 0), (15, 5), 5),
        ((0, 0), (10, 0), (5, -5), 5),
    ],
)
def test_distancer(a, b, c, distance):
    distance_function = distancer(a, b)
    actual_distance = distance_function(c)
    assert pytest.approx(actual_distance, 0.1) == distance


@pytest.mark.parametrize(
    "segment,tolerance,validity",
    [
        ([(10, 30), (20, 10), (30, 30)], 5, True),
        ([(10, 30), (20, 27), (30, 30)], 5, False),
        ([(10, 30), (20, 27), (30, 30), (40, 15), (50, 30)], 5, True),
    ],
)
def test_segment_validation(segment, tolerance, validity):
    assert validate_segment(segment, tolerance) == validity


def test_simplification_sanity():
    line = [(30, 10), (10, 30), (40, 40), (50, 30)]
    simplified_line = simplify(line, 5, 3)
    assert len(simplified_line) == 3
    assert simplified_line[0] == (30, 10)
    assert simplified_line[1] == (10, 30)
    assert simplified_line[2] == (50, 30)


def test_simplification_small_window():
    line = [(30, 10), (10, 30), (40, 40), (50, 30)]
    simplified_line = simplify(line, 5, 2)
    assert len(simplified_line) == 4


def test_simplification_short_line():
    line = [(30, 10), (10, 30), (40, 40), (50, 30)]
    simplified_line = simplify(line, 5, 6)
    assert len(simplified_line) == 4


def test_simplification_negative_tolerance():
    line = [(30, 10), (10, 30), (40, 40), (50, 30)]
    with pytest.raises(ValueError):
        simplify(line, -5, 6)


def test_simplification_equal_window():
    line = [(30, 10), (10, 30), (40, 40), (50, 30)]
    simplified_line = simplify(line, 5, 3)
    assert len(simplified_line) == 3
    assert simplified_line[0] == (30, 10)
    assert simplified_line[1] == (10, 30)
    assert simplified_line[2] == (50, 30)


def test_simplification_complex_line():
    line = [(10, 30), (15, 10), (20, 15), (25, 30), (30, 60), (35, 10), (40, 40)]
    simplified_line = simplify(line, 5, 3)
    assert len(simplified_line) == 5
    assert simplified_line[0] == (10, 30)
    assert simplified_line[1] == (15, 10)
    assert simplified_line[2] == (25, 30)
    assert simplified_line[3] == (30, 60)
    assert simplified_line[4] == (40, 40)
