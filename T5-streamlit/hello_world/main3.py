import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


"# My third streamlit app"
"Plot of $y = \sin(x) ^2$"


x = np.r_[0:2*np.pi:100j]
y = np.sin(x) ** 2
df = pd.DataFrame({
    'x': x,
    'y': y,
})
st.line_chart(y)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("The sine squared plot")
st.pyplot(fig)

p = px.line(df, 'x', 'y')
st.plotly_chart(p)

st.dataframe(df)

st.table(df.head(20))
