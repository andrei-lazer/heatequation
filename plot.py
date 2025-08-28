import heatcpp
import numpy as np
import streamlit as st
from streamlit_extras.grid import grid

from common import *
from create_plot import create_plot

with st.sidebar:
    st.title(page_icon + " " + page_title)
    n_xsteps = st.number_input(
        "Number of nodes in the $x$ direction",
        min_value=2,
        max_value=1000,
        step=1,
        value=101,
    )
    x_width = st.number_input(
        "Width of $x$ domain", min_value=1.0, max_value=20.0, step=0.1, value=10.0
    )
    alpha = st.number_input(
        "Diffusivity ($\\alpha$)",
        min_value=0.01,
        max_value=0.05,
        step=0.001,
        value=0.02,
    )
    dx = x_width / n_xsteps
    dt = dx**2 / (2 * alpha)
    final_t = st.number_input(
        "Final time",
        min_value=0.0,
        step=0.0001,
        max_value=dt * 10000,
        value=dt * 100,
        format="%0.4f",
    )
    n_iter = int(final_t / dt) + 1

st.title(page_title)

st.markdown("---")

st.info(
    "This app uses a C++ library made by me, which uses parallelism "
    "to solve the heat equation in one dimension. Feel free to explore how "
    "the heat equation solution varies with the parameters on the left, as "
    "well as the boundary conditions either side of the graph. Check out the "
    "other tabs below for more in depth explanations."
)

# tabs for the plot, and some explanations
# grid for the sliders and the plot
my_grid = grid(1, [1, 6, 1], 1, vertical_align="center")

# creating a container for a progress bar to be added in later
progress_container = my_grid.container()

# defining the solver - no  initial conditions yet
solver = heatcpp.Solver(n_xsteps, x_width, alpha, dt, n_iter)


def get_grid():
    grid = solver.array()
    return np.array(grid.data()).reshape(n_iter, n_xsteps)


# initial conditions
min_bounds = -10
max_bounds = 10
step = 1

left_bound = my_grid.number_input(
    "Left Boundary", min_value=min_bounds, max_value=max_bounds, step=step, value=-10
)

# plot goes in the middle - again, container for deferred creation
plot_cont = my_grid.container()

right_bound = my_grid.number_input(
    "Right Boundary", min_value=min_bounds, max_value=max_bounds, step=step, value=10
)


# initial condition is 0 everywhere except end points
def init_cond(x: float):
    if np.isclose(x, 0):
        return left_bound
    if np.isclose(x, x_width):
        return right_bound
    else:
        return 0


# x_grid for plotting
x_grid = np.linspace(0, x_width, n_xsteps)
# plotting!

with progress_container.status("Please wait...", expanded=True) as status:
    st.write("Setting initial condition...")
    solver.set_initial_condition(init_cond)

    st.write("Running C++ numerical solver...")
    solver.solve()

    st.write("Generating plot...")
    # Create plot is a huge function defined in create_plot.py.
    fig = create_plot(x_grid, get_grid(), x_width, dt, 200, "Heat Equation Solution")
    fig.update_xaxes(range=[-1, x_width + 1])
    fig.update_yaxes(range=[min_bounds - 1, max_bounds + 1])

    status.update(label="Done!", state="complete", expanded=False)

plot_cont.plotly_chart(fig)
