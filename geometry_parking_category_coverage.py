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
# Keep-alive comment: 2025-03-31 15:59:22.377703
# Keep-alive comment: 2025-03-31 19:25:00.126915
# Keep-alive comment: 2025-04-01 06:22:41.051236
# Keep-alive comment: 2025-04-01 17:23:35.652407
# Keep-alive comment: 2025-04-02 04:23:20.599932
# Keep-alive comment: 2025-04-02 15:23:19.823907
# Keep-alive comment: 2025-04-03 02:22:54.067069
# Keep-alive comment: 2025-04-03 13:24:00.227063
# Keep-alive comment: 2025-04-04 00:24:21.360750
# Keep-alive comment: 2025-04-04 11:23:52.687163
# Keep-alive comment: 2025-04-04 22:23:04.327519
# Keep-alive comment: 2025-04-05 09:22:54.383451
# Keep-alive comment: 2025-04-05 20:24:09.752184
# Keep-alive comment: 2025-04-06 07:23:39.359992
# Keep-alive comment: 2025-04-06 18:23:11.128508
# Keep-alive comment: 2025-04-07 05:23:34.969530
# Keep-alive comment: 2025-04-07 16:24:35.862812
# Keep-alive comment: 2025-04-08 03:23:51.123680
# Keep-alive comment: 2025-04-08 14:24:10.072950
# Keep-alive comment: 2025-04-09 01:23:34.385261
# Keep-alive comment: 2025-04-09 12:23:15.518348
# Keep-alive comment: 2025-04-09 23:23:34.585559
# Keep-alive comment: 2025-04-10 10:22:44.864674
# Keep-alive comment: 2025-04-10 21:23:08.130506
# Keep-alive comment: 2025-04-11 08:25:19.203915
# Keep-alive comment: 2025-04-11 19:25:40.037902
# Keep-alive comment: 2025-04-12 06:23:14.849223
# Keep-alive comment: 2025-04-12 17:23:28.321432
# Keep-alive comment: 2025-04-13 04:22:47.322667
# Keep-alive comment: 2025-04-13 15:23:42.635267
# Keep-alive comment: 2025-04-14 02:24:03.902410