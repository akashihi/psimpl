import pytest
from shapely import wkt
from psimpl import simplify, chunks, distancer


def test_chunks_sanity():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    chunked_seq = list(chunks(seq, 3))
    assert len(chunked_seq) == 5
    assert len(chunked_seq[0]) == 3
    assert len(chunked_seq[1]) == 3
    assert len(chunked_seq[2]) == 3
    assert len(chunked_seq[3]) == 3
    assert len(chunked_seq[4]) == 2
    assert chunked_seq[0][0] == 0
    assert chunked_seq[1][0] == 2
    assert chunked_seq[2][0] == 4
    assert chunked_seq[3][0] == 6
    assert chunked_seq[4][0] == 8


def test_chunks_boundary():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunked_seq = list(chunks(seq, 3))
    assert len(chunked_seq) == 5
    assert len(chunked_seq[4]) == 3
    assert chunked_seq[4][0] == 8
    assert chunked_seq[4][1] == 9
    assert chunked_seq[4][2] == 10


def test_small_seq_to_chunk():
    seq = [0, 1]
    chunked_seq = list(chunks(seq, 3))
    assert len(chunked_seq) == 1
    assert chunked_seq[0][0] == 0
    assert chunked_seq[0][1] == 1


def test_negative_chunk():
    seq = [0, 1, 2, 3]
    with pytest.raises(ValueError):
        next(chunks(seq, -2))


def test_empy_seq():
    seq = []
    chunked_seq = list(chunks(seq, 3))
    assert len(chunked_seq) == 0


@pytest.mark.parametrize("a,b,c,distance", [
    ((0, 0), (0, 10), (5, 5), 5),
    ((0, 0), (10, 0), (5, 5), 5),
    ((0, 0), (10, 0), (15, 5), 5),
    ((0, 0), (10, 0), (5, -5), 5),
])
def test_distancer(a, b, c, distance):
    distance_function = distancer(a, b)
    actual_distance = distance_function(c)
    assert pytest.approx(actual_distance, 0.1) == distance


def test_simplification_sanity():
    line = wkt.loads("LINESTRING (30 10, 10 30, 40 40, 50 30)")
    simplified_line = simplify(line.coords, 5, 3)
    assert len(simplified_line) == 3
    assert simplified_line[0] == (30, 10)
    assert simplified_line[1] == (40, 40)
    assert simplified_line[2] == (50, 30)


def test_simplification_small_window():
    line = wkt.loads("LINESTRING (30 10, 10 30, 40 40, 50 30)")
    simplified_line = simplify(line.coords, 5, 2)
    assert len(simplified_line) == 4


def test_simplification_short_line():
    line = wkt.loads("LINESTRING (30 10, 10 30, 40 40, 50 30)")
    simplified_line = simplify(line.coords, 5, 6)
    assert len(simplified_line) == 4


def test_simplification_negative_tolerance():
    line = wkt.loads("LINESTRING (30 10, 10 30, 40 40, 50 30)")
    with pytest.raises(ValueError):
        simplify(line.coords, -5, 6)


def test_simplification_equal_window():
    line = wkt.loads("LINESTRING (30 10, 10 30, 40 40, 50 30)")
    simplified_line = simplify(line.coords, 5, 4)
    assert len(simplified_line) == 3
    assert simplified_line[0] == (30, 10)
    assert simplified_line[1] == (10, 30)
    assert simplified_line[2] == (50, 30)


def test_simplification_complex_line():
    line = wkt.loads("LINESTRING (10 30, 15 10, 20 15, 25 30, 30 60, 35 10, 40 40)")
    simplified_line = simplify(line.coords, 5, 3)
    print(simplified_line)
