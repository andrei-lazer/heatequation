#include "Array2D.hpp"

template <typename T>
Array2D<T>::Array2D(size_t width, size_t height) :
	m_cols(width), m_rows(height), m_data(width*height)
{ }

template <typename T>
double& Array2D<T>::operator[](size_t i, size_t j)
{
	// numpy-like indexing, i.e. (row, column)
	return m_data[i*m_cols + j];
}

template <typename T>
const double& Array2D<T>::operator[](size_t i, size_t j) const
{
	return m_data[i*m_cols + j];
}

template class Array2D<double>;
