#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include "HeatSolver.hpp"
#include "Array2D.hpp"

namespace py = pybind11;

PYBIND11_MODULE(heatcpp, m) {
	m.doc() = "Heat Equation Solutions in C++";
	py::class_<Solver>(m, "Solver")
		.def(py::init<size_t, double, double, double, int>())
		.def("set_initial_condition", &Solver::set_initial_condition)
		.def("get_time", &Solver::get_time)
		.def("solve", &Solver::solve)
		.def("array", &Solver::array);

	py::class_<Array2D<double>>(m, "Array2D", py::buffer_protocol())
		.def(py::init<size_t, size_t>())
		.def("data", &Array2D<double>::data);
}
