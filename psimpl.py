def chunks(seq, n):
    """Splits sequence to n-sized chunks. Last chunk could be smaller than n.
    In case of a sequence shorter than n, single chunk containing the whole sequence
    will be returned. Each chunk (except first one) will start with a last element
    of a previous chunk

    :param seq: Sequence to split.
    :type seq: List
    :param n: Size of the chunk, should be > 0.
    type n: int

    :returns: Generator of chunks.

    :raises ValueError: When n is less than 1.
    """
    if n < 1:
        raise ValueError("Chunk size should be bigger than zero")

    for i in range(0, len(seq)-1, n-1):
        yield seq[i:i + n]


def simplify(points, tolerance, window):
    """Simplifies line using Lang algorithm. May decrease number of points.

    :param points: Line represented as array of points.
    :type points: array((int, int))
    :param tolerance: Simplification coefficient. Increasing the tolerance increases the similarity between
            incoming and simplified lines with price of a more complex simplified line(=less simplified).
    :param window: Size of the simplification window. This value constrains the simplification and
            sets minimal number of points to be returned (window - 1).
    :type window: int

    :returns: Simplified line represented as array of points.
    :rtype: array((int, int))
    """
    return points
