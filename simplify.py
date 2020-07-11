import argparse
from shapely import wkt
from shapely.geometry import LineString
from matplotlib import pyplot as plt
import psimpl


def simplify():
    parser = argparse.ArgumentParser(description="Line simplification tool. Accepts WKT ListString on stdin\n"
                                                 " and returns simplified WKT LineString on stdout")
    parser.add_argument("tolerance", type=float, help="Simplification tolerance.")
    parser.add_argument("window", type=int, help="Simplification window")
    parser.add_argument("--render", action="store_true", help="Render line images during processing")
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
            if args.render:
                plt.xlim(line_string.bounds[0], line_string.bounds[2])
                plt.ylim(line_string.bounds[1], line_string.bounds[3])
                fig, axs = plt.subplots(2)
                axs[0].plot(line_string, alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
                axs[1].plot(simplified_line_string, alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
                plt.show()
        except Exception as e:
            print("Error: {}\n".format(e))


if __name__ == '__main__':
    simplify()
