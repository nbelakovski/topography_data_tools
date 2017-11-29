#!/usr/bin/python3

import time
hardcoded_filename='WA_GlacierPeak_2014_001072.data'

# Using bindings (make sure to compile using ./build_bindigs.sh)
import tools
tstart = time.time()
matrix = tools.read_data(hardcoded_filename)
tend = time.time()
print("Successfully read", hardcoded_filename, "using bindings in {0:.2f} seconds".format(tend - tstart))
print(matrix)

import read_data
tstart = time.time()
matrix = read_data.read_data(hardcoded_filename)
tend = time.time()
print("Successfully read", hardcoded_filename, "using pure python in {0:.2f} seconds".format(tend - tstart))
print(matrix)

