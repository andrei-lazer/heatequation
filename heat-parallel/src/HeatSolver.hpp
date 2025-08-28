#pragma once

#include <memory>
#include <vector>
#include <functional>
#include <omp.h>
#include "Array2D.hpp"

class Solver
{
	const double alpha;
	const double dt;
	const double dx;
	const int n_iter;
	double curr_t;
	void check_stability() const;
	Array2D<double> m_array;
public:
	Solver(size_t num_points, double length, double alpha, double dt, int n_iter);
	void set_initial_condition(const std::function<double(double)>& init_func);

	void solve();

	double get_time() const { return curr_t; };
	const Array2D<double>& array() const { return m_array; }
};
