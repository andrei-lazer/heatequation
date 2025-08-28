from math import ceil

import numpy as np
import plotly.graph_objects as go
import streamlit as st


def create_plot(x_arr, y_grid, x_width, dt, max_frames, title):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_arr, y=y_grid[0], mode="lines", name="Solution"))
    fig.add_trace(
        go.Scatter(
            x=[0, x_width],
            y=[y_grid[0][0], y_grid[0][-1]],
            mode="markers",
            marker=dict(size=15),
            name="Boundaries",
        )
    )
    fig.update_layout(title=title, xaxis_title="x", yaxis_title="y")

    max_frames = 200
    n_frames = y_grid.shape[0]
    frame_skip = ceil(n_frames / max_frames)
    frame_indices = range(0, n_frames, frame_skip)
    frames = [
        go.Frame(
            data=[
                go.Scatter(x=x_arr, y=y_grid[i], mode="lines", name="Solution"),
                go.Scatter(
                    x=[0, x_width],
                    y=[y_grid[i][0], y_grid[i][-1]],
                    mode="markers",
                    marker=dict(size=15),
                    name="Boundaries",
                ),
            ],
            name=f"frame{i}",
            traces=[0, 1],  # Map frame data to the initial traces
        )
        for i in frame_indices
    ]
    fig.frames = frames

    # adding play-pause buttons, as well as a time slider.
    fig.update_layout(
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {
                                    "duration": dt * frame_skip * 1000,
                                    "redraw": True,
                                },
                                "fromcurrent": False,
                                "transition": {"duration": 0},
                            },
                        ],
                    ),
                    dict(
                        label="Pause",
                        method="animate",
                        args=[
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                                "transition": {"duration": 0},
                            },
                        ],
                    ),
                ],
            )
        ],
        sliders=[
            dict(
                steps=[
                    dict(
                        args=[
                            [f"frame{i}"],
                            {
                                "frame": {"duration": 300, "redraw": True},
                                "mode": "immediate",
                                "transition": {"duration": 300},
                            },
                        ],
                        label=f"t={i*dt:.3f}",  # Adjust time labels as needed
                        method="animate",
                    )
                    for i in frame_indices
                ],
                active=0,
                currentvalue={"prefix": "Time: "},
                pad={"t": 50},
            )
        ],
    )

    return fig
