# topography_data_tools
This repo contains code to read `.data` files from [TODO: insert kaggle link]. The file just contains a matrix of height points corresponding to pixels on the associated images.

# File layout

Field | Start offset (bytes) | Size (bytes)
------------ | ------------- | -----------
Number of rows | 0 | 4
Number of columns | 4 | 4
Item(0,0) | 8 | 4
Item(0,1) | 12 | 4
...|...|...
Item(1,0) | 8 + `columns` * 4 | 4
...|...|...
Item(r, c) | 8 + `rows` * `columns` * 4 | 4

Hopefully this notation is clear, if not please create an issue.

# Code

There are two options for reading the `.data` files:

1. Use read_data.py, which reads the file using pure Python code
2. Use the bindings, which link to compiled C++ code and are about 10x faster than the first option

To use the bindings, run `./build_bindings.sh` (assumes python3.5 and pybind11 installed via pip), or download them from the release.

# Examples

See example.py
