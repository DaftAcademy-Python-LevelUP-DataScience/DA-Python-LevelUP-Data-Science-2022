import sqlite3
import uuid

import pandas as pd
import streamlit as st
from sklearn.metrics import mean_squared_error


con = sqlite3.connect("results.db", check_same_thread=False)
stmt = "INSERT INTO results (nickname, email, score, filename) values (?, ?, ?, ?)"

y_true = pd.read_csv("y_true.csv").iloc[:, 0]

"# Week 4 Homework Checker"

with st.form("my_form"):
    student_nickname = st.text_input("Your nickname")
    student_email = st.text_input("Your e-mail", help="The one you've used for registration")
    uploaded_file = st.file_uploader("Upload your homework")
    submitted = st.form_submit_button("Submit")
    info_element = st.info("You must fill the name, mail and upload the file, then press `Submit`")
    if student_nickname != "" and student_email != "" and uploaded_file is not None and submitted:
        df = pd.read_csv(uploaded_file)
        filename = f"files/{uuid.uuid4()}.csv"
        df.to_csv(filename, index=False)
        y_pred = df['MEDV']
        score = mean_squared_error(y_true, y_pred)
        fields = (student_nickname, student_email, score, filename)
        with con:
            con.execute(stmt, fields)
        info_element.success("Result recorded")
    elif submitted:
        info_element.error("You must fill the name, mail and upload the file, then press `Submit`")

"## Top 10 Results:"

results = pd.read_sql_query("SELECT * FROM results", con)

if st.button("Refresh"):
    pass

st.table(
    results.sort_values("score")
    .groupby("email")
    .first()
    .reset_index()
    .loc[:, ["nickname", "score"]]
    .sort_values("score")
)
