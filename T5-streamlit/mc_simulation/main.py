import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def simulation(n):
    x = np.random.rand(n) * 4 - 2
    yr = np.random.rand(n)
    yf = np.exp(-(x**2))
    A = (yr < yf).mean() * 4

    fig, ax = plt.subplots()
    ax.plot(x[yf <= yr], yr[yf <= yr], ".b")
    ax.plot(x[yf > yr], yr[yf > yr], ".r")

    return fig, A


"# MC simulation"

"In this app we will calculate the area under function $\exp(-x^2)$ from $-2$ to $2$. "

n = st.number_input("n", value=1_000, min_value=1, max_value=10_000_000, format="%d")

if st.button("Simulate!"):
    with st.spinner(text="Simulating!"):
        fig, A = simulation(n)
        st.pyplot(fig)
        f"Calculated area of the function: {A.round(3)}"
