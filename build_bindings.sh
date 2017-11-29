#!/bin/bash -x
c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` bindings.cpp -o tools`python3.5-config --extension-suffix` read_data.cpp
