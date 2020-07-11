import math


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

    for i in range(0, len(seq) - 1, n - 1):
        yield seq[i:i + n]


def distancer(a, b):
    """ Generates a distance function, that will calculate distance from point C
    to the line, defined by points A and B.
    See https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line for details

    :param a: Point A coordinates
    :type a: Tuple(float, float)
    :param b: Point B coordinates
    :type b: Tuple(float, float)
    :returns: Function, that accept Tuple(float,float) with point C coordinates and calculates distance between C
        and AB line
    :rtype: func
    """
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    denominator = math.sqrt(math.pow(dy, 2) + math.pow(dx, 2))
    right_numerator = b[0]*a[1] - b[1]*a[0]

    def distance(c):
        return math.fabs(dy*c[0] - dx*c[1] + right_numerator)/denominator

    return distance


def simplify(points, tolerance, window):
    """Simplifies line using Lang algorithm. May decrease number of points.

    :param points: Line represented as array of points.
    :type points: array((int, int))
    :param tolerance: Simplification coefficient. Increasing the tolerance increases the similarity between
            incoming and simplified lines with price of a more complex simplified line(=less simplified).
    :param window: Size of the simplification window. This value constrains the simplification and
            sets minimal number of points to be returned (1/window).
    :type window: int

    :returns: Simplified line represented as array of points.
    :rtype: array((int, int))
    """
    if tolerance <= 0:
        raise ValueError("Tolerance have to be positive number")

    if window < 3 or len(points) < window:
        return points  # Nothing to simplify here

    output = []
    for segment in chunks(points, window):
        d_func = distancer(segment[0], segment[-1])
        filtered_points = list(filter(lambda c: d_func(c) > tolerance, segment[1:-2]))
        output.append(segment[0])
        output.extend(filtered_points)
    output.append(points[-1])  # We have to always add last point, as there is no next chunk starting with it
    return output
