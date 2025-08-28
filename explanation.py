import streamlit as st

from common import *

title = "Technical Details"
st.set_page_config(page_title=title, layout="centered")

st.title(title)

st.markdown(
    r"""
            # Heat Equation Report: Numerical Solution with FTCS and Parallelized C++ Implementation

            ## 1. What is the Heat Equation?
            The heat equation is a mathematical model used to describe how heat (or temperature) changes 
            over time and space in a material. It's a partial differential equation (PDE) that predicts temperature 
            distribution, commonly applied in physics and engineering, such as modeling heat flow in metals or diffusion 
            processes. In one dimension, it takes the form
    """
            )
st.latex(r"\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2},")
st.markdown(r"""
            where $u$ is temperature, $t$ is time, $x$ is position, and $\alpha$ is the thermal diffusivity (a material 
            property). This equation balances the rate of temperature change with how heat spreads spatially.


            **TL;DR**: The heat equation models how heat spreads in a material over time, used in physics and engineering 
            to predict temperature changes.

            ## 2. What is FTCS?
            FTCS stands for Forward-Time Centered-Space, a numerical method to solve the heat equation. It approximates 
            the equation's derivatives using discrete steps: time steps for how temperature evolves and spatial 
            steps for how it varies across a material. "Forward-Time" means it uses the current temperature to predict 
            the next time step, and "Centered-Space" means it calculates spatial changes using neighboring points
            . FTCS is simple but can be unstable if time and space steps aren't chosen carefully, requiring a stability 
            condition (e.g., small time steps relative to spatial steps).

            **TL;DR**: FTCS is a straightforward method to numerically solve the heat equation by breaking time 
            and space into small steps, though it needs careful tuning to avoid errors.

            ## 3. Overview of the C++ Implementation
            The C++ code (available on my [GitHub](https://github.com/your-repo-link)) solves the one
            -dimensional heat equation using the FTCS method. It discretizes a rod into a grid of points, initializes 
            temperatures (e.g., a hot spot or uniform temperature), and iteratively updates temperatures based on 
            the FTCS formula. To handle large grids efficiently, the code uses parallelization with 
            [OpenMP](https://www.openmp.org/), a tool for parallel computing in C++. OpenMP splits the computation 
            across multiple CPU cores, speeding up the process by dividing the grid updates among parallel threads
            . This is critical for performance in large-scale simulations, as it reduces computation time significantly.

            **TL;DR**: My C++ code solves the heat equation using FTCS, with OpenMP to parallelize calculations across 
            CPU cores for faster performance.

            For the full code and implementation details, please visit my [GitHub repository](https://github.com/your-repo-link).

            """
)
