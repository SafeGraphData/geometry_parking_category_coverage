import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(
    page_title="Geometry Summary Statistics - Parking Category Coverage",
    layout="wide"
)

#### Geometry Category Stats ####


category_stats_parking_df = read_from_gsheets('Parking - categories')\
    [["naics_code", "safegraph_category", "safegraph_subcategory", "total_open_poi_count", "total_parking_poi", "pct_poi_with_parking"]]\
    .astype({'naics_code': str})

category_stats_parking_df['total_open_poi_count'] =[int(x) for x in category_stats_parking_df['total_open_poi_count'] ]
category_stats_parking_df['total_parking_poi'] = [0 if (pd.isna(x)) or (x=="NaN")  else int(x) for x in category_stats_parking_df['total_parking_poi'] ]
category_stats_parking_df['pct_poi_with_parking'] = [0 if (pd.isna(x)) or (x=="NaN") else float(x) for x in category_stats_parking_df['pct_poi_with_parking'] ]
category_stats_parking_df['naics_code'] = [x.split(".")[0] for x in category_stats_parking_df['naics_code'] ]


df = (
    category_stats_parking_df
    .rename(columns={"naics_code": "NAICS Code", "safegraph_category": "SafeGraph Category",\
                        "safegraph_subcategory": "SafeGraph Subcategory", "total_open_poi_count": "Total Open POI Count",\
                           "pct_poi_with_parking":"Pct POI With Parking", "total_parking_poi":"Total Parking POI" })
    .assign(**{
        "Pct POI With Parking": lambda df: ((df["Pct POI With Parking"]) * 100).astype(float)
}).sort_values('Total Open POI Count', ascending=False)
    .reset_index(drop=True)
)

df['Total Open POI Count'] = df['Total Open POI Count'].astype(int).apply(lambda x: "{:,}".format(x))
df['Pct POI With Parking'] = df['Pct POI With Parking'].astype(float).apply(lambda x: "{:.01f}%".format(x))
df['Total Parking POI'] = df['Total Parking POI'].astype(int).apply(lambda x: "{:,}".format(x))

styled_df = (
    df.style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
)

st.write("Parking Coverage by Category")
st.dataframe(styled_df, use_container_width=True, hide_index=True)


hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-03-29 14:27:24.475786