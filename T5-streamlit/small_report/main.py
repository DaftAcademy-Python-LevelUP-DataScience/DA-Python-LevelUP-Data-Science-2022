import pandas as pd
import streamlit as st
import plotly.express as px

st.config.dataFrameSerialization = "arrow"


@st.cache
def load_data():
    flights = pd.read_csv("../../data/flights.csv", engine="pyarrow")
    flights["DATE"] = pd.to_datetime(
        flights["YEAR"].astype(str) + "-" + flights["MONTH"].astype(str) + "-" + flights["DAY"].astype(str)
    )
    airports = pd.read_csv("../../data/airports.csv", engine="pyarrow")
    return flights, airports


flights, airports = load_data()

"# Small flights application"

"Let's recall some analysis from earlier classes."

airport_input = st.text_input("Airport")

flights_lax = (
    flights.query("DESTINATION_AIRPORT == @airport_input")
    .groupby("ORIGIN_AIRPORT")
    .agg({"ARRIVAL_DELAY": ["mean", "count"]})
    .reset_index()
    .merge(airports, left_on="ORIGIN_AIRPORT", right_on="IATA_CODE")
    # .loc[:, ["AIRPORT","ARRIVAL_DELAY", "Count"]]
)

st.write(flights_lax)

flights_d = flights.query("DESTINATION_AIRPORT == @airport_input").value_counts("DATE").reset_index().sort_values("DATE").rename(columns={0: "Count"})

p = px.line(flights_d, "DATE", "Count")

st.plotly_chart(p)
