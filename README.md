# Lang simplification algorithm in Python

The Lang simplification algorithm defines a fixed size search-region. The first and last points of that search region 
form a segment. This segment is used to calculate the perpendicular distance to each intermediate point. 
If any calculated distance is larger than the specified tolerance, the search region will be shrunk by excluding its 
last point. This process will continue untill all calculated distances fall below the specified tolerance, 
or when there are no more intermediate points. All intermediate points are removed and a new search region 
is defined starting at the last point from old search region.

Algorithm is implemented in Python.

## Building from source

You'll need python 3.8 and pipenv installed. Do usual pipenv dance to get dependencies and that's all:

    sudo apt-get install python3-tk # Optional, only if you need a standalone render functionality
    pipenv install
    pipenv shell
    pytest

## Building with docker

In case you don't want to pollute your system in python or would like to run it somewhere, you can build a Docker image:

    docker build -f Dockerfile -t psimpl ./

## Running it

Simplification tool _requires_ two positional arguments:

* tolerance, floating point number - a simplification tolerance. The bigger it is, the more points will be left on 
    a simplified line.
* window, integer positive number - a simplification window. The bigger it is, the more aggressive simplifications will be.
    It is guaranteed that 1/window fraction of points will be left on the line.
    
Tool also supports optional `render` argument, that turns on instant visualization of original and simplified lines.

To run the tool you could either run it with python or docker, depending on your build choice:
    python simplify.py 3.0 3 --render
or
    docker run -it psimpl 3.0 3
    
Running tool expects a WKT LineString on stdin and will return simplified line in form of WKT LineString on stdout:

    $ python simplify.py 3.0 3   
    Type a correct WKT LineString or type Q/q to quit
    --> LINESTRING(10 30, 15 10, 20 15, 25 30, 30 60, 35 10, 40 40)
    LINESTRING (10 30, 15 10, 25 30, 30 60, 40 40)
    --> q                                                                              

You can use Q to quit the tool.

## Authors

* **Denis Chaplygin** - *Initial work* - [akashihi](https://github.com/akashihi)

## License

This project is licensed under the GPLv3 License - see the LICENSE file for details.