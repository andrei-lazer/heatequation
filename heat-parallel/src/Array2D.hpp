#pragma once
#include <memory>
#include <vector>
#include <functional>

template <typename T>
class Array2D
{
	size_t m_cols;
	size_t m_rows;
	std::vector<T> m_data;
public:
	Array2D(size_t width, size_t height);
	double& operator()(size_t i, size_t j);
	const double& operator()(size_t i, size_t j) const;
	size_t cols() const { return m_cols; };
	size_t rows() const { return m_rows; };
	std::vector<T> data() const { return m_data; };
};
