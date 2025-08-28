#include "HeatSolver.hpp"
#include <cassert>
#include <stdexcept>
#include <iostream>
#include <cmath>

// Solver

Solver::Solver(size_t num_points, double length, double alpha, double dt, int n_iter) :
	alpha(alpha),dt(dt),dx(length/((double)num_points-1)), n_iter(n_iter), curr_t(0),m_array(num_points, n_iter)
{
	if (dt <= 0)
	{
		throw std::invalid_argument("dt must be > 0");
	}
	if (dx <= 0)
	{
		throw std::invalid_argument("dx must be > 0");
	}
	if (alpha <= 0)
	{
		throw std::invalid_argument("alpha must be > 0");
	}
	if (n_iter <= 0)
	{
		throw std::invalid_argument("n_iter must be >= 1");
	}
	check_stability();
}

void Solver::check_stability() const
{
	double von_neumann_quantity =alpha *dt / (dx*dx);
	if (von_neumann_quantity > 0.5)
	{
		std::cout << "dt*alpha/(dx^2) needs to be < 1/2. Currently " << von_neumann_quantity << std::endl;
	}
}

void Solver::set_initial_condition(const std::function<double(double)>& init_func)
{
	for (size_t j = 0; j < m_array.cols(); ++j)
	{
		double new_val = init_func(j*dx);
		m_array(0,j) = new_val;
	}
}

void Solver::solve()
{
	double mult = alpha * dt / (dx*dx);

	// iteration ove time
#pragma omp parallel for
	for (size_t i = 1; i < m_array.rows(); ++i)
	{
		// iteration over space
		for (size_t j = 1; j < m_array.cols() - 1; ++j)
		{
			double adding = mult * (m_array(i-1,j+1) - 2.0*m_array(i-1,j) +m_array(i-1,j-1));
			m_array(i,j) =m_array(i-1,j) + adding;
		}
		m_array(i,0) = m_array(i-1,0);
		m_array(i,m_array.cols()-1) = m_array(i-1,m_array.cols()-1);
	curr_t += dt;
	}
}
