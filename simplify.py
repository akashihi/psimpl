import argparse
from shapely import wkt
from shapely.geometry import LineString
import psimpl


def simplify():
    parser = argparse.ArgumentParser(description="Line simplification tool. Accepts WKT ListString on stdin\n"
                                                 " and returns simplified WKT LineString on stdout")
    parser.add_argument("tolerance", type=float, help="Simplification tolerance.")
    parser.add_argument("window", type=int, help="Simplification window")
    args = parser.parse_args()

    print("Type a correct WKT LineString or type Q/q to quit")
    while True:
        line = input("--> ")
        if line.upper().startswith("Q"):
            break

        try:
            line_string = wkt.loads(line)
            simplified_line = psimpl.simplify(line_string.coords, args.tolerance, args.window)
            simplified_line_string = LineString(simplified_line)
            print(simplified_line_string.wkt)
        except Exception as e:
            print("Error: {}\n".format(e))


if __name__ == '__main__':
    simplify()
