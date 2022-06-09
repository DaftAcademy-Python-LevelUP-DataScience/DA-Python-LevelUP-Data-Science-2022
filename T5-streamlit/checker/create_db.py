import sqlite3

con = sqlite3.connect("results.db")

with con:
    con.execute(
        """CREATE TABLE results
               (nickname text, email text, score real, filename text)"""
    )
