# 🔥 Heat Equation Solver

This project implements a numerical solution to the one-dimensional heat equation using the Forward-Time Centered-Space (FTCS) method, powered by 
a C++ backend and visualized through an interactive Streamlit web application.

Check it out at <a href="https://heatequation.streamlit.app" target="_blank">https://heatequation.streamlit.app</a>.

## 🚀 Features
- **Numerical Solution**: Solves the 1D heat equation, 

    $$
        \frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2},
    $$

using the FTCS method to model heat distribution over time, where $u$ is 
temperature, $t$ is time, $x$ is position, and $\alpha$ is thermal diffusivity.
- **C++ Backend**: Uses a custom 2-D grid template and OpenMP for parallel processing to quickly
  approximate solutions to the heat equation using FTCS.
- **Python Dashboard**: Interactive Python-based web dashboard built with Streamlit, connected to
the C++ backend using pybind11.
- **Customizable Parameters**: Adjust grid size, time steps, and thermal diffusivity to explore various 
simulation scenarios.

## 🔧 Local Hosting

### Requirements: 
- python version >= 3.12

### Steps
1. Clone the repository: `git clone https://github.com/andrei-lazer/heatequation.git`
2. `cd heatequation`
3. (Recommended) create a virtual environment and activate it:

    `python -m venv venv && source venv/bin/activate`
3. Install all required external packages: `pip install streamlit numpy streamlit_extras pybind11`
4. Install the C++ heat equation solving package: `pip install ./heat-parallel`
5. Run the app using streamlit: `streamlit run main.py`

Note: Do not use `requirements.txt`, since it is made for mounting on the Streamlit community
cloud. While I'm sure this is fixable, the workaround is not particularly time consuming.
