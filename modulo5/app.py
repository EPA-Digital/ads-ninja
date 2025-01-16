import streamlit as st
import polars as pl

st.title("Hola!")

df = pl.read_csv("modulo5/data.csv")
df = df.drop_nulls()
clean_df = df.with_columns(
    (pl.col("date").str.to_date("%Y-%m-%d", exact=False).alias("date")),
    (pl.col("cost").str.replace_all("\\$|,","").cast(pl.Float32).alias("cost"))
)
st.write(clean_df)
df_grouped = clean_df.group_by("date").agg(pl.col("cost").sum())
st.write(df_grouped)