import json

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Favorite dish", page_icon="🥘")

with open("dishes.json") as f:
    dishes = json.load(f)

st.title("What is your favorite dish?")
st.write("Pick from the list or add your own")
form = st.form(key="dish")
available_dishes = sorted(dishes.keys())
dish_radio = form.selectbox("Pick from the list", available_dishes)
dish_text = form.text_input(
    "Or type if it's not on the list:",
    placeholder="Leave empty to choose from the list",
)
submit = form.form_submit_button("Submit")

if submit:
    if dish_text != "":
        key = dish_text.lower().capitalize()
    else:
        key = dish_radio

    if key not in dishes:
        dishes[key] = 1
    else:
        dishes[key] += 1

    with open("dishes.json", "w") as f:
        json.dump(dishes, f)

if st.button("Refresh"):
    pass
df = pd.DataFrame(dishes.items(), columns=["Dish", "Count"])
st.plotly_chart(px.bar(df, x="Dish", y="Count"))
