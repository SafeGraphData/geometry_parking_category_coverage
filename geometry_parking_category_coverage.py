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
# Keep-alive comment: 2025-04-14 13:23:28.180567
# Keep-alive comment: 2025-04-15 00:23:13.120870
# Keep-alive comment: 2025-04-15 11:23:35.277364
# Keep-alive comment: 2025-04-15 22:23:18.832773
# Keep-alive comment: 2025-04-16 09:23:58.082095
# Keep-alive comment: 2025-04-16 20:23:48.183060
# Keep-alive comment: 2025-04-17 07:23:19.267486
# Keep-alive comment: 2025-04-17 18:25:42.954323
# Keep-alive comment: 2025-04-18 05:23:03.561929
# Keep-alive comment: 2025-04-18 16:23:09.040603
# Keep-alive comment: 2025-04-19 03:23:33.763523
# Keep-alive comment: 2025-04-19 14:22:44.680240
# Keep-alive comment: 2025-04-20 01:22:43.266371
# Keep-alive comment: 2025-04-20 12:23:38.052479
# Keep-alive comment: 2025-04-20 23:23:12.951687
# Keep-alive comment: 2025-04-21 10:23:59.265946
# Keep-alive comment: 2025-04-21 21:23:22.971361
# Keep-alive comment: 2025-04-22 08:23:33.804472
# Keep-alive comment: 2025-04-22 19:23:36.967074
# Keep-alive comment: 2025-04-23 06:23:07.862171
# Keep-alive comment: 2025-04-23 17:23:21.471840
# Keep-alive comment: 2025-04-24 04:23:14.185028
# Keep-alive comment: 2025-04-24 15:24:10.559859
# Keep-alive comment: 2025-04-25 02:22:47.997803
# Keep-alive comment: 2025-04-25 13:24:09.248698
# Keep-alive comment: 2025-04-25 16:08:20.296209
# Keep-alive comment: 2025-04-25 16:18:14.981984
# Keep-alive comment: 2025-04-26 00:23:49.409493
# Keep-alive comment: 2025-04-26 11:23:44.535451
# Keep-alive comment: 2025-04-26 22:22:43.737017
# Keep-alive comment: 2025-04-27 09:23:14.559998
# Keep-alive comment: 2025-04-27 20:23:09.241064
# Keep-alive comment: 2025-04-28 07:23:31.200980
# Keep-alive comment: 2025-04-28 18:23:59.431346
# Keep-alive comment: 2025-04-29 05:23:29.498070
# Keep-alive comment: 2025-04-29 16:24:13.435784
# Keep-alive comment: 2025-04-30 03:23:04.040572
# Keep-alive comment: 2025-04-30 14:23:17.710253
# Keep-alive comment: 2025-05-01 01:23:43.392458
# Keep-alive comment: 2025-05-01 12:23:14.171497
# Keep-alive comment: 2025-05-01 23:22:47.179602
# Keep-alive comment: 2025-05-02 10:23:33.538416
# Keep-alive comment: 2025-05-02 21:22:44.962683
# Keep-alive comment: 2025-05-03 08:23:08.501663
# Keep-alive comment: 2025-05-03 19:23:27.900205
# Keep-alive comment: 2025-05-04 06:23:33.318968
# Keep-alive comment: 2025-05-04 17:22:42.643744
# Keep-alive comment: 2025-05-05 04:23:52.980184
# Keep-alive comment: 2025-05-05 15:23:10.592855
# Keep-alive comment: 2025-05-06 02:24:03.555175
# Keep-alive comment: 2025-05-06 13:23:04.160460
# Keep-alive comment: 2025-05-07 00:23:03.815711
# Keep-alive comment: 2025-05-07 11:23:04.066613
# Keep-alive comment: 2025-05-07 22:23:14.640202
# Keep-alive comment: 2025-05-08 09:23:07.164315
# Keep-alive comment: 2025-05-08 20:23:05.778517
# Keep-alive comment: 2025-05-09 07:23:14.378501
# Keep-alive comment: 2025-05-09 18:23:35.473516
# Keep-alive comment: 2025-05-10 05:23:13.031645
# Keep-alive comment: 2025-05-10 16:23:07.272034
# Keep-alive comment: 2025-05-11 03:23:07.484016
# Keep-alive comment: 2025-05-11 14:22:59.354327
# Keep-alive comment: 2025-05-12 01:23:04.651151
# Keep-alive comment: 2025-05-12 12:23:34.211628
# Keep-alive comment: 2025-05-12 23:23:07.998205
# Keep-alive comment: 2025-05-13 10:24:06.295244
# Keep-alive comment: 2025-05-13 21:23:08.315014
# Keep-alive comment: 2025-05-14 08:23:33.953610
# Keep-alive comment: 2025-05-14 19:23:33.667455
# Keep-alive comment: 2025-05-15 06:23:34.978750
# Keep-alive comment: 2025-05-15 17:23:58.920631
# Keep-alive comment: 2025-05-16 04:23:20.227511
# Keep-alive comment: 2025-05-16 15:22:22.872389
# Keep-alive comment: 2025-05-17 02:22:41.762161
# Keep-alive comment: 2025-05-17 13:23:15.505472
# Keep-alive comment: 2025-05-18 00:22:40.220774
# Keep-alive comment: 2025-05-18 11:23:08.375499
# Keep-alive comment: 2025-05-18 22:23:05.804352
# Keep-alive comment: 2025-05-19 09:23:40.661786
# Keep-alive comment: 2025-05-19 20:22:40.346918
# Keep-alive comment: 2025-05-20 07:22:56.405328
# Keep-alive comment: 2025-05-20 18:24:08.559434
# Keep-alive comment: 2025-05-21 05:22:40.876960
# Keep-alive comment: 2025-05-21 16:22:49.310034
# Keep-alive comment: 2025-05-22 03:22:44.199084
# Keep-alive comment: 2025-05-22 14:22:43.645306
# Keep-alive comment: 2025-05-23 01:22:46.221441
# Keep-alive comment: 2025-05-23 12:22:46.173084
# Keep-alive comment: 2025-05-23 23:22:50.716698