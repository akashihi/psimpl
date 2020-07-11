import math


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
    right_numerator = b[0] * a[1] - b[1] * a[0]

    def distance(c):
        return math.fabs(dy * c[0] - dx * c[1] + right_numerator) / denominator

    return distance


def validate_segment(segment, tolerance):
    """Checks if simplification segment needs to be simplified,
    by testing distances between first-last line and other points

    :param segment: Line segment to test
    :type segment: array((int, int))
    :param tolerance: Simplification coefficient. Increasing the tolerance increases the similarity between
            incoming and simplified lines with price of a more complex simplified line(=less simplified).
    :type tolerance: float

    :returns: True is segment can be simplified, False otherwise
    :rtype: bool
    """
    d_func = distancer(segment[0], segment[-1])
    for p in segment[1:-1]:
        if d_func(p) > tolerance:
            return True
    return False


def simplify(points, tolerance, window):
    """Simplifies line using Lang algorithm. May decrease number of points.

    :param points: Line represented as array of points.
    :type points: array((int, int))
    :param tolerance: Simplification coefficient. Increasing the tolerance increases the similarity between
            incoming and simplified lines with price of a more complex simplified line(=less simplified).
    :type tolerance: float
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
    pos = 0
    while pos < len(points):
        segment_len = window
        while (
            validate_segment(points[pos : pos + 1 + segment_len], tolerance)
            and segment_len > 2
        ):
            segment_len -= 1
        output.extend(points[pos : pos + segment_len])
        if segment_len < window:
            del points[pos + segment_len : pos + window]
        pos += segment_len
    return output
