#include "pybind11/pybind11.h"
#include "pybind11/numpy.h"
#include "read_data.hpp"

namespace py = pybind11;


PYBIND11_MODULE(tools, module)
{
  module.def("read_data", &tools::read_data, "read rows and columns from the provided .data file, returns numpy array");
}
