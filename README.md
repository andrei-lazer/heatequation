# 🔥 Heat Equation Solver

This project implements a numerical solution to the one-dimensional heat equation using the Forward-Time Centered-Space (FTCS) method, powered by 
a C++ backend and visualized through an interactive Streamlit web application.

## 🚀 Features
- **Numerical Solution**: Solves the 1D heat equation, $\frac{\partial u}{\partial t} = \alpha \frac{\
partial^2 u}{\partial x^2}$, using the FTCS method to model heat distribution over time, where $u$ is 
temperature, $t$ is time, $x$ is position, and $\alpha$ is thermal diffusivity.
- **C++ Backend**: Efficient computation with a C++ implementation, utilizing [OpenMP](https://www.openmp
.org/) for parallel processing across multiple CPU cores to handle large grids quickly.
- **Streamlit Dashboard**: Interactive Python-based web dashboard built with Streamlit.
- **Customizable Parameters**: Adjust grid size, time steps, and thermal diffusivity to explore various 
simulation scenarios.

## 🔧 Usage
1. Clone the repository: `git clone https://github.com/andrei-lazer/heatequation.git`
2. Run the Streamlit app: `streamlit run app.py`
3. Configure simulation parameters (e.g., grid points, time steps) in the web interface.
4. Visualize the heat distribution and interact with the results.
