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
# Keep-alive comment: 2025-05-24 10:22:48.656645
# Keep-alive comment: 2025-05-24 21:22:45.463622
# Keep-alive comment: 2025-05-25 08:22:45.709139
# Keep-alive comment: 2025-05-25 19:22:50.455212
# Keep-alive comment: 2025-05-26 06:22:35.462768
# Keep-alive comment: 2025-05-26 17:22:40.120788
# Keep-alive comment: 2025-05-27 04:22:45.683683
# Keep-alive comment: 2025-05-27 15:22:49.844587
# Keep-alive comment: 2025-05-28 02:22:59.821144
# Keep-alive comment: 2025-05-28 13:22:48.084969
# Keep-alive comment: 2025-05-29 00:22:43.894791
# Keep-alive comment: 2025-05-29 11:22:38.588448
# Keep-alive comment: 2025-05-29 22:22:53.503671
# Keep-alive comment: 2025-05-30 09:22:38.103714
# Keep-alive comment: 2025-05-30 20:22:38.920500
# Keep-alive comment: 2025-05-31 07:22:50.701197
# Keep-alive comment: 2025-05-31 18:22:46.367436
# Keep-alive comment: 2025-06-01 05:22:44.627407
# Keep-alive comment: 2025-06-01 16:22:58.161105
# Keep-alive comment: 2025-06-02 03:22:59.510896
# Keep-alive comment: 2025-06-02 14:22:50.021244
# Keep-alive comment: 2025-06-03 01:22:40.637213
# Keep-alive comment: 2025-06-03 12:22:54.535012
# Keep-alive comment: 2025-06-03 23:22:49.368964
# Keep-alive comment: 2025-06-04 10:22:49.916098
# Keep-alive comment: 2025-06-04 21:22:28.474140
# Keep-alive comment: 2025-06-05 08:22:52.396657
# Keep-alive comment: 2025-06-05 19:22:41.926595
# Keep-alive comment: 2025-06-06 06:22:40.271216
# Keep-alive comment: 2025-06-06 17:22:23.541128
# Keep-alive comment: 2025-06-07 04:22:25.453320
# Keep-alive comment: 2025-06-07 15:22:34.859016
# Keep-alive comment: 2025-06-08 02:22:40.126366
# Keep-alive comment: 2025-06-08 13:22:41.622564
# Keep-alive comment: 2025-06-09 00:22:24.303602
# Keep-alive comment: 2025-06-09 11:22:38.794119
# Keep-alive comment: 2025-06-09 22:22:46.877759
# Keep-alive comment: 2025-06-10 09:22:50.044845
# Keep-alive comment: 2025-06-10 20:22:43.251262
# Keep-alive comment: 2025-06-11 07:22:44.358252
# Keep-alive comment: 2025-06-11 18:24:31.068239
# Keep-alive comment: 2025-06-12 05:22:41.476831
# Keep-alive comment: 2025-06-12 16:22:44.744344
# Keep-alive comment: 2025-06-13 03:22:45.760561
# Keep-alive comment: 2025-06-13 14:22:34.859894
# Keep-alive comment: 2025-06-14 01:22:54.872827
# Keep-alive comment: 2025-06-14 12:22:42.255874
# Keep-alive comment: 2025-06-14 23:22:33.640928
# Keep-alive comment: 2025-06-15 10:22:19.363795
# Keep-alive comment: 2025-06-15 21:22:54.179233
# Keep-alive comment: 2025-06-16 08:22:50.607203
# Keep-alive comment: 2025-06-16 19:22:34.618445
# Keep-alive comment: 2025-06-17 06:23:11.554387
# Keep-alive comment: 2025-06-17 17:22:39.402882
# Keep-alive comment: 2025-06-18 04:22:46.087952
# Keep-alive comment: 2025-06-18 15:22:42.761949
# Keep-alive comment: 2025-06-19 02:22:43.521399
# Keep-alive comment: 2025-06-19 13:22:42.516475
# Keep-alive comment: 2025-06-20 00:22:40.011659
# Keep-alive comment: 2025-06-20 11:23:29.155674
# Keep-alive comment: 2025-06-20 22:22:48.923767
# Keep-alive comment: 2025-06-21 09:22:34.431423
# Keep-alive comment: 2025-06-21 20:22:46.350394
# Keep-alive comment: 2025-06-22 07:22:39.437635
# Keep-alive comment: 2025-06-22 18:22:29.969163
# Keep-alive comment: 2025-06-23 05:22:46.522498
# Keep-alive comment: 2025-06-23 16:22:39.455285
# Keep-alive comment: 2025-06-24 03:22:45.967612
# Keep-alive comment: 2025-06-24 14:22:24.689879
# Keep-alive comment: 2025-06-25 01:22:19.443193
# Keep-alive comment: 2025-06-25 12:22:41.103103
# Keep-alive comment: 2025-06-25 23:22:44.151338
# Keep-alive comment: 2025-06-26 10:22:51.406835
# Keep-alive comment: 2025-06-26 21:24:15.313114
# Keep-alive comment: 2025-06-27 08:22:44.589873
# Keep-alive comment: 2025-06-27 19:22:41.596544
# Keep-alive comment: 2025-06-28 06:22:49.068500
# Keep-alive comment: 2025-06-28 17:22:39.324343
# Keep-alive comment: 2025-06-29 04:22:28.164513
# Keep-alive comment: 2025-06-29 15:22:19.024937
# Keep-alive comment: 2025-06-30 02:22:40.379061
# Keep-alive comment: 2025-06-30 13:22:21.107312
# Keep-alive comment: 2025-07-01 00:24:26.106663
# Keep-alive comment: 2025-07-01 11:22:41.080410
# Keep-alive comment: 2025-07-01 22:22:45.576787
# Keep-alive comment: 2025-07-02 09:22:39.275929
# Keep-alive comment: 2025-07-02 20:24:28.062054
# Keep-alive comment: 2025-07-03 07:22:54.099866
# Keep-alive comment: 2025-07-03 18:22:18.940190
# Keep-alive comment: 2025-07-04 05:22:42.842936
# Keep-alive comment: 2025-07-04 16:22:38.881529
# Keep-alive comment: 2025-07-05 03:22:38.140587
# Keep-alive comment: 2025-07-05 14:22:43.228442
# Keep-alive comment: 2025-07-06 01:22:40.390463
# Keep-alive comment: 2025-07-06 12:22:37.866977
# Keep-alive comment: 2025-07-06 23:22:39.102380
# Keep-alive comment: 2025-07-07 10:22:39.191951
# Keep-alive comment: 2025-07-07 21:22:37.875661
# Keep-alive comment: 2025-07-08 08:22:43.022068
# Keep-alive comment: 2025-07-08 19:22:38.552317
# Keep-alive comment: 2025-07-09 06:22:49.913546
# Keep-alive comment: 2025-07-09 17:23:22.966026
# Keep-alive comment: 2025-07-10 04:22:38.367836
# Keep-alive comment: 2025-07-10 15:22:43.415208
# Keep-alive comment: 2025-07-11 02:22:37.441298
# Keep-alive comment: 2025-07-11 13:22:38.189395
# Keep-alive comment: 2025-07-12 00:22:24.663685
# Keep-alive comment: 2025-07-12 11:22:42.887956
# Keep-alive comment: 2025-07-12 22:22:39.057101
# Keep-alive comment: 2025-07-13 09:22:38.862979
# Keep-alive comment: 2025-07-13 20:22:23.262422
# Keep-alive comment: 2025-07-14 07:22:34.964962
# Keep-alive comment: 2025-07-14 18:22:58.122466
# Keep-alive comment: 2025-07-15 05:22:48.831600
# Keep-alive comment: 2025-07-15 16:22:43.050629
# Keep-alive comment: 2025-07-16 03:22:43.183580
# Keep-alive comment: 2025-07-16 14:22:43.272388
# Keep-alive comment: 2025-07-17 01:22:38.618519
# Keep-alive comment: 2025-07-17 12:22:44.615527
# Keep-alive comment: 2025-07-17 23:22:37.100585
# Keep-alive comment: 2025-07-18 10:22:58.295103
# Keep-alive comment: 2025-07-18 21:22:38.100297
# Keep-alive comment: 2025-07-19 08:23:18.784403
# Keep-alive comment: 2025-07-19 19:22:23.451696
# Keep-alive comment: 2025-07-20 06:22:48.284886
# Keep-alive comment: 2025-07-20 17:22:54.191155
# Keep-alive comment: 2025-07-21 04:22:48.511009
# Keep-alive comment: 2025-07-21 15:22:34.608042
# Keep-alive comment: 2025-07-22 02:22:57.812737
# Keep-alive comment: 2025-07-22 13:23:10.593684
# Keep-alive comment: 2025-07-23 00:22:44.930745
# Keep-alive comment: 2025-07-23 11:22:34.040463
# Keep-alive comment: 2025-07-23 22:22:37.791363
# Keep-alive comment: 2025-07-24 09:22:53.510641
# Keep-alive comment: 2025-07-24 20:22:39.484510
# Keep-alive comment: 2025-07-25 07:22:33.674887
# Keep-alive comment: 2025-07-25 18:22:38.702366
# Keep-alive comment: 2025-07-26 05:22:33.843719
# Keep-alive comment: 2025-07-26 16:22:38.367849
# Keep-alive comment: 2025-07-27 03:22:33.357120
# Keep-alive comment: 2025-07-27 14:22:23.986509
# Keep-alive comment: 2025-07-28 01:22:44.863821
# Keep-alive comment: 2025-07-28 12:22:39.534051
# Keep-alive comment: 2025-07-28 23:22:38.097134
# Keep-alive comment: 2025-07-29 10:22:12.906986
# Keep-alive comment: 2025-07-29 21:22:43.930316
# Keep-alive comment: 2025-07-30 08:22:39.999116
# Keep-alive comment: 2025-07-30 19:22:48.216126
# Keep-alive comment: 2025-07-31 06:22:53.317369
# Keep-alive comment: 2025-07-31 17:22:39.022312
# Keep-alive comment: 2025-08-01 04:22:37.567300
# Keep-alive comment: 2025-08-01 15:22:48.371358
# Keep-alive comment: 2025-08-02 02:22:33.287064
# Keep-alive comment: 2025-08-02 13:22:43.664741
# Keep-alive comment: 2025-08-03 00:22:39.230135
# Keep-alive comment: 2025-08-03 11:22:44.146489
# Keep-alive comment: 2025-08-03 22:22:39.013760
# Keep-alive comment: 2025-08-04 09:22:35.324147
# Keep-alive comment: 2025-08-04 20:22:38.982916
# Keep-alive comment: 2025-08-05 07:22:42.014124
# Keep-alive comment: 2025-08-05 18:22:43.459376
# Keep-alive comment: 2025-08-06 05:22:38.342774
# Keep-alive comment: 2025-08-06 16:24:28.942650
# Keep-alive comment: 2025-08-07 03:22:43.035397
# Keep-alive comment: 2025-08-07 14:22:44.140105
# Keep-alive comment: 2025-08-08 01:22:33.319655
# Keep-alive comment: 2025-08-08 12:22:44.304690
# Keep-alive comment: 2025-08-08 23:22:44.688236
# Keep-alive comment: 2025-08-09 10:22:38.272681
# Keep-alive comment: 2025-08-09 21:23:00.381822
# Keep-alive comment: 2025-08-10 08:22:44.653076
# Keep-alive comment: 2025-08-10 19:22:44.679872
# Keep-alive comment: 2025-08-11 06:22:38.754228
# Keep-alive comment: 2025-08-11 17:22:43.945912
# Keep-alive comment: 2025-08-12 04:22:43.343662
# Keep-alive comment: 2025-08-12 15:22:35.094194
# Keep-alive comment: 2025-08-13 02:22:44.093419
# Keep-alive comment: 2025-08-13 13:22:39.352587
# Keep-alive comment: 2025-08-14 00:22:37.645462
# Keep-alive comment: 2025-08-14 11:22:44.943951
# Keep-alive comment: 2025-08-14 22:22:38.708360
# Keep-alive comment: 2025-08-15 09:22:38.473753
# Keep-alive comment: 2025-08-15 20:22:27.928066
# Keep-alive comment: 2025-08-16 07:22:52.993110
# Keep-alive comment: 2025-08-16 18:22:39.234169
# Keep-alive comment: 2025-08-17 05:22:42.418440
# Keep-alive comment: 2025-08-17 16:22:37.641911
# Keep-alive comment: 2025-08-18 03:22:38.888240
# Keep-alive comment: 2025-08-18 14:22:39.657749
# Keep-alive comment: 2025-08-19 01:22:39.145708
# Keep-alive comment: 2025-08-19 12:22:44.093019
# Keep-alive comment: 2025-08-19 23:23:05.995288
# Keep-alive comment: 2025-08-20 10:22:40.442710
# Keep-alive comment: 2025-08-20 21:22:43.622377
# Keep-alive comment: 2025-08-21 08:22:40.549748
# Keep-alive comment: 2025-08-21 19:22:44.394659
# Keep-alive comment: 2025-08-22 06:22:44.172840
# Keep-alive comment: 2025-08-22 17:22:39.239740
# Keep-alive comment: 2025-08-23 04:22:48.661140
# Keep-alive comment: 2025-08-23 15:22:37.621204
# Keep-alive comment: 2025-08-24 02:22:37.889555
# Keep-alive comment: 2025-08-24 13:22:38.690824
# Keep-alive comment: 2025-08-25 00:22:45.214927
# Keep-alive comment: 2025-08-25 11:22:43.712548
# Keep-alive comment: 2025-08-25 22:22:38.736391
# Keep-alive comment: 2025-08-26 09:22:39.493721
# Keep-alive comment: 2025-08-26 20:22:43.555915
# Keep-alive comment: 2025-08-27 07:22:48.781552
# Keep-alive comment: 2025-08-27 18:22:18.876089
# Keep-alive comment: 2025-08-28 05:22:49.464990
# Keep-alive comment: 2025-08-28 16:22:38.913126
# Keep-alive comment: 2025-08-29 03:22:23.020108
# Keep-alive comment: 2025-08-29 14:22:28.742912
# Keep-alive comment: 2025-08-30 01:22:28.257794
# Keep-alive comment: 2025-08-30 12:22:23.769863
# Keep-alive comment: 2025-08-30 23:22:27.398239
# Keep-alive comment: 2025-08-31 10:22:23.190910
# Keep-alive comment: 2025-08-31 21:22:34.880921
# Keep-alive comment: 2025-09-01 08:22:36.472985
# Keep-alive comment: 2025-09-01 19:22:34.855359
# Keep-alive comment: 2025-09-02 06:22:23.266745
# Keep-alive comment: 2025-09-02 17:22:34.535282
# Keep-alive comment: 2025-09-03 04:22:27.475578
# Keep-alive comment: 2025-09-03 15:22:29.638251
# Keep-alive comment: 2025-09-04 02:22:33.077482
# Keep-alive comment: 2025-09-04 13:22:39.125846
# Keep-alive comment: 2025-09-05 00:22:24.058620
# Keep-alive comment: 2025-09-05 11:22:19.119824
# Keep-alive comment: 2025-09-05 22:22:28.211880
# Keep-alive comment: 2025-09-06 09:22:24.607950
# Keep-alive comment: 2025-09-06 20:22:23.367655
# Keep-alive comment: 2025-09-07 07:22:29.436138
# Keep-alive comment: 2025-09-07 18:22:29.442610
# Keep-alive comment: 2025-09-08 05:22:25.460336
# Keep-alive comment: 2025-09-08 16:22:29.760703
# Keep-alive comment: 2025-09-09 03:22:54.839916
# Keep-alive comment: 2025-09-09 14:22:29.984903
# Keep-alive comment: 2025-09-10 01:22:22.913369
# Keep-alive comment: 2025-09-10 12:22:34.640117
# Keep-alive comment: 2025-09-10 23:22:23.641528
# Keep-alive comment: 2025-09-11 10:22:26.404206
# Keep-alive comment: 2025-09-11 21:22:24.204929
# Keep-alive comment: 2025-09-12 08:22:38.871037
# Keep-alive comment: 2025-09-12 19:22:29.242420
# Keep-alive comment: 2025-09-13 06:22:18.114210
# Keep-alive comment: 2025-09-13 17:22:24.507931
# Keep-alive comment: 2025-09-14 04:22:14.520922
# Keep-alive comment: 2025-09-14 15:22:25.755941
# Keep-alive comment: 2025-09-15 02:22:23.113907
# Keep-alive comment: 2025-09-15 13:22:25.243018
# Keep-alive comment: 2025-09-16 00:22:24.219911
# Keep-alive comment: 2025-09-16 11:22:29.467276
# Keep-alive comment: 2025-09-16 22:22:23.256147
# Keep-alive comment: 2025-09-17 09:22:25.290507
# Keep-alive comment: 2025-09-17 20:22:34.518834
# Keep-alive comment: 2025-09-18 07:22:31.160662
# Keep-alive comment: 2025-09-18 18:22:30.361544
# Keep-alive comment: 2025-09-19 05:22:24.887918
# Keep-alive comment: 2025-09-19 16:22:59.285092
# Keep-alive comment: 2025-09-20 03:22:29.001567
# Keep-alive comment: 2025-09-20 14:22:29.930498
# Keep-alive comment: 2025-09-21 01:22:29.400938
# Keep-alive comment: 2025-09-21 12:22:29.213890
# Keep-alive comment: 2025-09-21 23:22:24.553506
# Keep-alive comment: 2025-09-22 10:22:26.986482
# Keep-alive comment: 2025-09-22 21:22:23.517145
# Keep-alive comment: 2025-09-23 08:22:26.128279
# Keep-alive comment: 2025-09-23 19:22:30.728712
# Keep-alive comment: 2025-09-24 06:22:24.496132
# Keep-alive comment: 2025-09-24 17:22:28.975466
# Keep-alive comment: 2025-09-25 04:24:42.824329
# Keep-alive comment: 2025-09-25 15:22:34.289897
# Keep-alive comment: 2025-09-26 02:22:30.072621
# Keep-alive comment: 2025-09-26 13:22:33.844923
# Keep-alive comment: 2025-09-26 19:31:01.211747
# Keep-alive comment: 2025-09-27 05:31:06.909132
# Keep-alive comment: 2025-09-27 15:31:01.362398
# Keep-alive comment: 2025-09-28 01:31:05.579815
# Keep-alive comment: 2025-09-28 11:31:06.452669
# Keep-alive comment: 2025-09-28 21:31:05.633882
# Keep-alive comment: 2025-09-29 07:31:12.225540
# Keep-alive comment: 2025-09-29 17:31:21.853542
# Keep-alive comment: 2025-09-30 03:31:00.674920
# Keep-alive comment: 2025-09-30 13:31:06.800011
# Keep-alive comment: 2025-09-30 23:31:25.911652
# Keep-alive comment: 2025-10-01 09:31:32.110882
# Keep-alive comment: 2025-10-01 19:31:06.393847
# Keep-alive comment: 2025-10-02 05:31:34.931953
# Keep-alive comment: 2025-10-02 15:31:32.230917
# Keep-alive comment: 2025-10-03 01:31:05.725472
# Keep-alive comment: 2025-10-03 11:31:27.018822
# Keep-alive comment: 2025-10-03 21:31:00.786548
# Keep-alive comment: 2025-10-04 07:31:00.998984
# Keep-alive comment: 2025-10-04 17:31:10.872472
# Keep-alive comment: 2025-10-05 03:31:05.918189
# Keep-alive comment: 2025-10-05 13:31:11.085517
# Keep-alive comment: 2025-10-05 23:31:31.185774
# Keep-alive comment: 2025-10-06 09:31:36.731347
# Keep-alive comment: 2025-10-06 19:31:07.912143
# Keep-alive comment: 2025-10-07 05:31:08.152070
# Keep-alive comment: 2025-10-07 15:31:29.244183
# Keep-alive comment: 2025-10-08 01:31:06.655931
# Keep-alive comment: 2025-10-08 11:31:07.647542
# Keep-alive comment: 2025-10-08 21:31:07.252549
# Keep-alive comment: 2025-10-09 07:31:09.388771
# Keep-alive comment: 2025-10-09 17:31:08.935444
# Keep-alive comment: 2025-10-10 03:30:57.059762
# Keep-alive comment: 2025-10-10 13:30:48.238348
# Keep-alive comment: 2025-10-10 23:31:01.114623
# Keep-alive comment: 2025-10-11 09:31:07.281843
# Keep-alive comment: 2025-10-11 19:31:00.955346
# Keep-alive comment: 2025-10-12 05:31:04.061045
# Keep-alive comment: 2025-10-12 15:31:08.627171
# Keep-alive comment: 2025-10-13 01:31:03.076506
# Keep-alive comment: 2025-10-13 11:31:34.383692
# Keep-alive comment: 2025-10-13 21:30:57.156841
# Keep-alive comment: 2025-10-14 07:31:01.044521
# Keep-alive comment: 2025-10-14 17:31:03.928503
# Keep-alive comment: 2025-10-15 03:31:01.233425
# Keep-alive comment: 2025-10-15 13:31:03.032203
# Keep-alive comment: 2025-10-15 23:31:06.694481
# Keep-alive comment: 2025-10-16 09:31:02.785542
# Keep-alive comment: 2025-10-16 19:31:08.410244
# Keep-alive comment: 2025-10-17 05:31:07.268850
# Keep-alive comment: 2025-10-17 15:31:23.902870
# Keep-alive comment: 2025-10-18 01:31:02.591110
# Keep-alive comment: 2025-10-18 11:31:27.476124
# Keep-alive comment: 2025-10-18 21:31:37.248450
# Keep-alive comment: 2025-10-19 07:30:57.419876
# Keep-alive comment: 2025-10-19 17:31:32.168482
# Keep-alive comment: 2025-10-20 03:31:29.441041
# Keep-alive comment: 2025-10-20 13:31:07.880909
# Keep-alive comment: 2025-10-20 23:31:02.474675
# Keep-alive comment: 2025-10-21 09:31:08.021038
# Keep-alive comment: 2025-10-21 19:33:08.376112
# Keep-alive comment: 2025-10-22 05:31:03.287259
# Keep-alive comment: 2025-10-22 15:32:08.449502
# Keep-alive comment: 2025-10-23 01:31:02.244154
# Keep-alive comment: 2025-10-23 11:31:14.689495
# Keep-alive comment: 2025-10-23 21:31:03.636815
# Keep-alive comment: 2025-10-24 07:32:23.647040
# Keep-alive comment: 2025-10-24 17:31:13.038623
# Keep-alive comment: 2025-10-25 03:31:07.692959
# Keep-alive comment: 2025-10-25 13:31:31.628043
# Keep-alive comment: 2025-10-25 23:31:03.350186
# Keep-alive comment: 2025-10-26 09:30:56.886175
# Keep-alive comment: 2025-10-26 19:31:33.765463
# Keep-alive comment: 2025-10-27 05:31:13.998630
# Keep-alive comment: 2025-10-27 15:31:28.621059
# Keep-alive comment: 2025-10-28 01:31:06.536233
# Keep-alive comment: 2025-10-28 11:31:08.808092
# Keep-alive comment: 2025-10-28 21:30:57.155071
# Keep-alive comment: 2025-10-29 07:31:04.076655
# Keep-alive comment: 2025-10-29 17:31:12.904979
# Keep-alive comment: 2025-10-30 03:31:02.711756
# Keep-alive comment: 2025-10-30 13:31:34.146248
# Keep-alive comment: 2025-10-30 23:31:08.955694
# Keep-alive comment: 2025-10-31 09:32:23.140999
# Keep-alive comment: 2025-10-31 19:30:58.545496
# Keep-alive comment: 2025-11-01 05:31:07.274252
# Keep-alive comment: 2025-11-01 15:30:56.363585
# Keep-alive comment: 2025-11-02 01:31:07.734431
# Keep-alive comment: 2025-11-02 11:31:09.577513
# Keep-alive comment: 2025-11-02 21:31:23.378827
# Keep-alive comment: 2025-11-03 07:31:03.780336
# Keep-alive comment: 2025-11-03 17:31:07.320989
# Keep-alive comment: 2025-11-04 03:31:07.760950
# Keep-alive comment: 2025-11-04 13:31:35.176180
# Keep-alive comment: 2025-11-04 23:31:26.965079
# Keep-alive comment: 2025-11-05 09:31:38.565620
# Keep-alive comment: 2025-11-05 19:31:07.712258
# Keep-alive comment: 2025-11-06 05:31:33.096806
# Keep-alive comment: 2025-11-06 15:31:20.975628
# Keep-alive comment: 2025-11-07 01:31:05.934536
# Keep-alive comment: 2025-11-07 11:31:10.364156
# Keep-alive comment: 2025-11-07 21:31:09.635410
# Keep-alive comment: 2025-11-08 07:30:57.665823
# Keep-alive comment: 2025-11-08 17:31:13.417027
# Keep-alive comment: 2025-11-09 03:31:47.551888
# Keep-alive comment: 2025-11-09 13:31:08.619687
# Keep-alive comment: 2025-11-09 23:30:58.075987
# Keep-alive comment: 2025-11-10 09:31:03.663715
# Keep-alive comment: 2025-11-10 19:31:19.631462
# Keep-alive comment: 2025-11-11 05:31:04.900319
# Keep-alive comment: 2025-11-11 15:31:02.205708
# Keep-alive comment: 2025-11-12 01:31:10.215115
# Keep-alive comment: 2025-11-12 11:31:11.861499
# Keep-alive comment: 2025-11-12 21:31:28.641381
# Keep-alive comment: 2025-11-13 07:30:52.122309
# Keep-alive comment: 2025-11-13 17:31:04.028234
# Keep-alive comment: 2025-11-14 03:31:10.651373
# Keep-alive comment: 2025-11-14 13:31:31.841046
# Keep-alive comment: 2025-11-14 23:31:03.451418
# Keep-alive comment: 2025-11-15 09:31:07.487894
# Keep-alive comment: 2025-11-15 19:31:12.828699
# Keep-alive comment: 2025-11-16 05:31:04.188740
# Keep-alive comment: 2025-11-16 15:31:08.983814
# Keep-alive comment: 2025-11-17 01:30:58.505965
# Keep-alive comment: 2025-11-17 11:31:32.509914
# Keep-alive comment: 2025-11-17 21:30:59.610532
# Keep-alive comment: 2025-11-18 07:31:02.741355
# Keep-alive comment: 2025-11-18 17:31:03.237800
# Keep-alive comment: 2025-11-19 03:31:06.955171
# Keep-alive comment: 2025-11-19 13:30:59.196812
# Keep-alive comment: 2025-11-19 23:31:01.409161
# Keep-alive comment: 2025-11-20 09:31:08.993413
# Keep-alive comment: 2025-11-20 19:32:58.401711
# Keep-alive comment: 2025-11-21 05:31:04.225372
# Keep-alive comment: 2025-11-21 15:31:08.703566
# Keep-alive comment: 2025-11-22 01:31:12.857895
# Keep-alive comment: 2025-11-22 11:30:58.112642
# Keep-alive comment: 2025-11-22 21:31:08.548867
# Keep-alive comment: 2025-11-23 07:31:09.337612
# Keep-alive comment: 2025-11-23 17:31:11.413014
# Keep-alive comment: 2025-11-24 03:31:02.861868
# Keep-alive comment: 2025-11-24 13:30:58.737227
# Keep-alive comment: 2025-11-24 23:31:09.020374
# Keep-alive comment: 2025-11-25 09:31:30.720168
# Keep-alive comment: 2025-11-25 19:31:04.585581
# Keep-alive comment: 2025-11-26 05:31:14.399900
# Keep-alive comment: 2025-11-26 15:31:13.195970
# Keep-alive comment: 2025-11-27 01:31:08.574195
# Keep-alive comment: 2025-11-27 11:31:04.752933
# Keep-alive comment: 2025-11-27 21:30:59.083537
# Keep-alive comment: 2025-11-28 07:30:57.751890
# Keep-alive comment: 2025-11-28 17:31:09.363023
# Keep-alive comment: 2025-11-29 03:31:03.770189
# Keep-alive comment: 2025-11-29 13:31:14.018185
# Keep-alive comment: 2025-11-29 23:31:03.625057
# Keep-alive comment: 2025-11-30 09:31:05.682843
# Keep-alive comment: 2025-11-30 19:30:53.848682
# Keep-alive comment: 2025-12-01 05:30:53.538462
# Keep-alive comment: 2025-12-01 15:30:59.915136
# Keep-alive comment: 2025-12-02 01:30:43.674650
# Keep-alive comment: 2025-12-02 11:31:05.700056
# Keep-alive comment: 2025-12-02 21:31:07.934879
# Keep-alive comment: 2025-12-03 07:31:05.200707
# Keep-alive comment: 2025-12-03 17:31:12.881001
# Keep-alive comment: 2025-12-04 03:31:03.210495
# Keep-alive comment: 2025-12-04 13:31:00.377846
# Keep-alive comment: 2025-12-04 23:31:03.032317
# Keep-alive comment: 2025-12-05 09:31:03.083639
# Keep-alive comment: 2025-12-05 19:30:57.903733
# Keep-alive comment: 2025-12-06 05:31:03.952655
# Keep-alive comment: 2025-12-06 15:30:50.745436
# Keep-alive comment: 2025-12-07 01:31:00.079917
# Keep-alive comment: 2025-12-07 11:31:03.357346
# Keep-alive comment: 2025-12-07 21:30:59.819813
# Keep-alive comment: 2025-12-08 07:31:13.047779
# Keep-alive comment: 2025-12-08 17:30:58.598732
# Keep-alive comment: 2025-12-09 03:31:03.122573
# Keep-alive comment: 2025-12-09 13:31:01.620958
# Keep-alive comment: 2025-12-09 23:31:03.532926
# Keep-alive comment: 2025-12-10 09:31:04.928244
# Keep-alive comment: 2025-12-10 19:31:09.383671
# Keep-alive comment: 2025-12-11 05:30:44.093374
# Keep-alive comment: 2025-12-11 15:31:05.602329
# Keep-alive comment: 2025-12-12 01:31:03.278592
# Keep-alive comment: 2025-12-12 11:30:49.263050
# Keep-alive comment: 2025-12-12 21:31:08.787919
# Keep-alive comment: 2025-12-13 07:31:02.749127
# Keep-alive comment: 2025-12-13 17:31:04.560757
# Keep-alive comment: 2025-12-14 03:31:06.906841
# Keep-alive comment: 2025-12-14 13:31:02.492909
# Keep-alive comment: 2025-12-14 23:30:57.642076
# Keep-alive comment: 2025-12-15 09:31:02.799384
# Keep-alive comment: 2025-12-15 19:31:02.498676
# Keep-alive comment: 2025-12-16 05:31:10.404738
# Keep-alive comment: 2025-12-16 15:30:57.926695
# Keep-alive comment: 2025-12-17 01:31:28.932919
# Keep-alive comment: 2025-12-17 11:30:57.680142
# Keep-alive comment: 2025-12-17 21:34:13.107373
# Keep-alive comment: 2025-12-18 07:31:04.595277
# Keep-alive comment: 2025-12-18 17:31:12.514714
# Keep-alive comment: 2025-12-19 03:31:08.588295
# Keep-alive comment: 2025-12-19 13:31:02.786441
# Keep-alive comment: 2025-12-19 23:31:42.232016
# Keep-alive comment: 2025-12-20 09:30:48.064887
# Keep-alive comment: 2025-12-20 19:31:03.753940
# Keep-alive comment: 2025-12-21 05:31:01.846241
# Keep-alive comment: 2025-12-21 15:30:47.003903
# Keep-alive comment: 2025-12-22 01:31:01.353854
# Keep-alive comment: 2025-12-22 11:31:04.149820
# Keep-alive comment: 2025-12-22 21:30:47.977848
# Keep-alive comment: 2025-12-23 07:31:05.140233
# Keep-alive comment: 2025-12-23 17:31:06.985840
# Keep-alive comment: 2025-12-24 03:30:53.587111
# Keep-alive comment: 2025-12-24 13:30:48.700173
# Keep-alive comment: 2025-12-24 23:30:55.923871
# Keep-alive comment: 2025-12-25 09:31:09.315795
# Keep-alive comment: 2025-12-25 19:31:02.826289
# Keep-alive comment: 2025-12-26 05:31:02.914108
# Keep-alive comment: 2025-12-26 15:31:02.306472
# Keep-alive comment: 2025-12-27 01:30:56.313602
# Keep-alive comment: 2025-12-27 11:31:01.422650
# Keep-alive comment: 2025-12-27 21:31:02.836805
# Keep-alive comment: 2025-12-28 07:31:02.085598
# Keep-alive comment: 2025-12-28 17:31:09.431102
# Keep-alive comment: 2025-12-29 03:30:57.037360
# Keep-alive comment: 2025-12-29 13:31:03.603876
# Keep-alive comment: 2025-12-29 23:30:58.147460
# Keep-alive comment: 2025-12-30 09:30:48.136586
# Keep-alive comment: 2025-12-30 19:31:06.596307
# Keep-alive comment: 2025-12-31 05:30:59.168501
# Keep-alive comment: 2025-12-31 15:31:00.060256
# Keep-alive comment: 2026-01-01 01:31:08.951644
# Keep-alive comment: 2026-01-01 11:31:03.965213
# Keep-alive comment: 2026-01-01 21:31:15.312240
# Keep-alive comment: 2026-01-02 07:31:05.447736
# Keep-alive comment: 2026-01-02 17:31:02.629699
# Keep-alive comment: 2026-01-03 03:31:00.058547
# Keep-alive comment: 2026-01-03 13:31:05.117578
# Keep-alive comment: 2026-01-03 23:31:06.712543
# Keep-alive comment: 2026-01-04 09:30:58.932628
# Keep-alive comment: 2026-01-04 19:31:05.045169
# Keep-alive comment: 2026-01-05 05:31:03.721819
# Keep-alive comment: 2026-01-05 15:31:08.730886
# Keep-alive comment: 2026-01-06 01:30:58.451532
# Keep-alive comment: 2026-01-06 11:30:59.751028
# Keep-alive comment: 2026-01-06 21:30:59.040868
# Keep-alive comment: 2026-01-07 07:30:58.353638
# Keep-alive comment: 2026-01-07 17:30:57.436921
# Keep-alive comment: 2026-01-08 03:31:06.172838
# Keep-alive comment: 2026-01-08 13:30:59.974642
# Keep-alive comment: 2026-01-08 23:30:58.036160
# Keep-alive comment: 2026-01-09 09:30:58.882012
# Keep-alive comment: 2026-01-09 19:31:03.485821
# Keep-alive comment: 2026-01-10 05:31:07.518097
# Keep-alive comment: 2026-01-10 15:30:52.658010
# Keep-alive comment: 2026-01-11 01:31:00.112449
# Keep-alive comment: 2026-01-11 11:31:08.499639
# Keep-alive comment: 2026-01-11 21:31:02.857178
# Keep-alive comment: 2026-01-12 07:31:05.098526
# Keep-alive comment: 2026-01-12 17:31:02.267873
# Keep-alive comment: 2026-01-13 03:31:00.089377
# Keep-alive comment: 2026-01-13 13:30:54.363683
# Keep-alive comment: 2026-01-13 23:31:07.231577
# Keep-alive comment: 2026-01-14 09:30:59.880755
# Keep-alive comment: 2026-01-14 19:31:03.550420
# Keep-alive comment: 2026-01-15 05:31:03.004894
# Keep-alive comment: 2026-01-15 15:31:05.519581
# Keep-alive comment: 2026-01-16 01:31:06.961478
# Keep-alive comment: 2026-01-16 11:31:14.449272
# Keep-alive comment: 2026-01-16 21:31:01.858963
# Keep-alive comment: 2026-01-17 07:30:47.404148
# Keep-alive comment: 2026-01-17 17:31:02.308196
# Keep-alive comment: 2026-01-18 03:31:03.479001
# Keep-alive comment: 2026-01-18 13:30:58.472876
# Keep-alive comment: 2026-01-18 23:31:08.112632
# Keep-alive comment: 2026-01-19 09:31:06.373521
# Keep-alive comment: 2026-01-19 19:31:01.651800
# Keep-alive comment: 2026-01-20 05:30:57.238068
# Keep-alive comment: 2026-01-20 15:31:03.620197