import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import zipfile
from io import BytesIO
import numpy as np
import pandas as pd
import folium
from streamlit_folium import folium_static


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    custom_data = pd.read_csv(uploaded_file)
    # Perform visualization on custom_data
# Import and display raw data
def read_data(platform):
    return pd.read_csv(platform)
# Sample data
fb_data = read_data("cleaned_data_Facebook.csv")
insta_data = read_data("cleaned_data_Instragram.csv")
twitter_data = read_data("cleaned_data_Twitter.csv")
tiktok_data = read_data("cleaned_data_TikTok.csv")
yt_data = read_data("cleaned_data_YouTube.csv")
thrd_data = read_data("cleaned_data_Threads.csv")

zip_buffer = BytesIO()

# Create a ZipFile object
with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
    # Add each CSV file to the zip file
    zip_file.writestr('Facebook_data.csv', fb_data.to_csv(index=False))
    zip_file.writestr('Instagram_data.csv', insta_data.to_csv(index=False))
    zip_file.writestr('Twitter_data.csv', twitter_data.to_csv(index=False))
    zip_file.writestr('TikTok_data.csv', tiktok_data.to_csv(index=False))
    zip_file.writestr('YouTube_data.csv', yt_data.to_csv(index=False))
    zip_file.writestr('Threads_data.csv', thrd_data.to_csv(index=False))

# Download Zip Button for all data
st.download_button(label='Download All Data as CSV Files', data=zip_buffer.getvalue(), file_name='All_data.zip', mime='application/zip')

# Advanced Sidebar
st.sidebar.markdown('**<font color="#ffc72c">User Input Features</font>**', unsafe_allow_html=True)
st.sidebar.markdown("*Select the social media platform you want to analyze:*")

# Multiselect for social media
input_media = st.sidebar.multiselect('Social Media', ["Facebook", "Instagram", "Threads", "Tiktok", "Twitter", "Youtube"])
# Load country location data
country_loc_data = pd.read_csv("country_loc.csv", encoding='latin1')

# Simplified Pydeck map
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=country_loc_data,
            get_position='[Longitude, Latitude]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
), use_container_width=True)


# Date Range Selector
st.sidebar.subheader("Date Range Selector")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2022-01-01'))
end_date = st.sidebar.date_input("End Date", pd.to_datetime('2022-12-31'))

# Follower Count Threshold Slider
st.sidebar.subheader("Follower Count Threshold")
follower_threshold = st.sidebar.slider("Select Follower Count Threshold", min_value=0, max_value=100000, value=5000, step=100)

# Theme Customization
st.sidebar.subheader("Theme Customization")
theme_options = ['Light', 'Dark']
selected_theme = st.sidebar.radio('Select Theme', theme_options)

# Apply custom CSS based on the selected theme
if selected_theme == 'Dark':
    st.markdown("""
        <style>
            body {
                background-color: #2E2E2E;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body {
                background-color: white;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)

# Reset button to clear filters
if st.sidebar.button("Reset Filters"):
    st.experimental_rerun()

# Rest of your code...


if input_media == ['Facebook']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Facebook
    st.subheader("Bar Chart - Total Followers Count for Facebook")
    fig_fb_bar = px.bar(fb_data, x="Name (English)", y="Facebook Follower #", title="Total Followers Count for Facebook")
    st.plotly_chart(fig_fb_bar)

    # Add a download button for the Bar Chart
    if st.button("Download Facebook Bar Chart Data"):
        st.write("Downloading Facebook Bar Chart Data...")
        csv_data = fig_fb_bar.to_csv(index=False)
        st.download_button(
            label='Download Bar Chart Data as CSV',
            data=csv_data,
            file_name='Facebook_Bar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 3: Donut Chart for Facebook
    st.subheader("Donut Chart - Distribution of Followers for Facebook")
    fig_fb_donut = px.pie(fb_data, names="Region of Focus", title="Distribution of Followers for Facebook", hole=0.4)
    st.plotly_chart(fig_fb_donut)

    # Add a download button for the Donut Chart
    if st.button("Download Facebook Donut Chart Data"):
        st.write("Downloading Facebook Donut Chart Data...")
        csv_data = fig_fb_donut.to_csv(index=False)
        st.download_button(
            label='Download Donut Chart Data as CSV',
            data=csv_data,
            file_name='Facebook_Donut_Chart_Data.csv',
            mime='text/csv'
        )
     
     
    # Visualization 4: Radar Chart - Multidimensional Comparison for Facebook
    st.subheader("Radar Chart - Multidimensional Comparison for Facebook")
    fig_fb_radar = px.line_polar(fb_data, r="Facebook Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Facebook")
    st.plotly_chart(fig_fb_radar)

    # Add a download button for the Radar Chart
    if st.button("Download Facebook Radar Chart Data"):
        st.write("Downloading Facebook Radar Chart Data...")
        csv_data = fig_fb_radar.to_csv(index=False)
        st.download_button(
            label='Download Radar Chart Data as CSV',
            data=csv_data,
            file_name='Facebook_Radar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 5: Sunburst Chart - Proportional Representation for Facebook
    st.subheader("Sunburst Chart - Proportional Representation for Facebook")
    fig_fb_sunburst = px.sunburst(fb_data, path=["Region of Focus"], values="Facebook Follower #", title="Proportional Representation of Follower Counts for Facebook")
    st.plotly_chart(fig_fb_sunburst)

    # Add a download button for the Sunburst Chart
    if st.button("Download Facebook Sunburst Chart Data"):
        st.write("Downloading Facebook Sunburst Chart Data...")
        csv_data = fig_fb_sunburst.to_csv(index=False)
        st.download_button(
            label='Download Sunburst Chart Data as CSV',
            data=csv_data,
            file_name='Facebook_Sunburst_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 7: Treemap - Proportional Representation of Total Followers for Facebook
    st.subheader("Treemap - Proportional Representation of Total Followers for Facebook")
    fig_fb_treemap_total_followers = px.treemap(fb_data, path=["Region of Focus", "Name (English)"], values="Facebook Follower #",
                                                title="Proportional Representation of Total Followers by Region for Facebook")
    st.plotly_chart(fig_fb_treemap_total_followers)

    # Add a download button for the Treemap
    if st.button("Download Facebook Treemap Data"):
        st.write("Downloading Facebook Treemap Data...")
        csv_data = fig_fb_treemap_total_followers.to_csv(index=False)
        st.download_button(
            label='Download Treemap Data as CSV',
            data=csv_data,
            file_name='Facebook_Treemap_Data.csv',
            mime='text/csv'
        )

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatter_global_distribution = px.scatter_3d(fb_data, x="Region of Focus", y="Name (English)", z="Facebook Follower #",
                                                    color="Facebook Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatter_global_distribution)

    # Add a download button for the 3D Scatter Plot
    if st.button("Download Facebook 3D Scatter Plot Data"):
        st.write("Downloading Facebook 3D Scatter Plot Data...")
        csv_data = fig_3d_scatter_global_distribution.to_csv(index=False)
        st.download_button(
            label='Download 3D Scatter Plot Data as CSV',
            data=csv_data,
            file_name='Facebook_3D_Scatter_Plot_Data.csv',
            mime='text/csv'
        )



elif input_media == ['Instagram']:
    st.markdown('No precise Data for Instagram for graphical evaluation !!!!')
    st.markdown('Select another social media from the sidebar on your left. Thank You.')

    # Placeholder visualizations
    # Visualization 1: Bar Chart
    st.subheader("Placeholder Bar Chart for Instagram")
    fig_insta_bar = px.bar(title="Placeholder Bar Chart for Instagram")
    st.plotly_chart(fig_insta_bar)

    # Visualization 2: Pie Chart
    st.subheader("Placeholder Pie Chart for Instagram")
    fig_insta_pie = px.pie(title="Placeholder Pie Chart for Instagram", values=[1], names=["Placeholder"])
    st.plotly_chart(fig_insta_pie)

    # Visualization 3: Line Chart
    st.subheader("Placeholder Line Chart for Instagram")
    fig_insta_line = px.line(title="Placeholder Line Chart for Instagram")
    st.plotly_chart(fig_insta_line)

    # Add download buttons for the visualizations
    if st.button("Download Placeholder Bar Chart Data"):
        st.write("Downloading Placeholder Bar Chart Data...")
        csv_data = fig_insta_bar.to_csv(index=False)
        st.download_button(
            label='Download Placeholder Bar Chart Data as CSV',
            data=csv_data,
            file_name='Instagram_Placeholder_Bar_Chart_Data.csv',
            mime='text/csv'
        )

    if st.button("Download Placeholder Pie Chart Data"):
        st.write("Downloading Placeholder Pie Chart Data...")
        csv_data = fig_insta_pie.to_csv(index=False)
        st.download_button(
            label='Download Placeholder Pie Chart Data as CSV',
            data=csv_data,
            file_name='Instagram_Placeholder_Pie_Chart_Data.csv',
            mime='text/csv'
        )

    if st.button("Download Placeholder Line Chart Data"):
        st.write("Downloading Placeholder Line Chart Data...")
        csv_data = fig_insta_line.to_csv(index=False)
        st.download_button(
            label='Download Placeholder Line Chart Data as CSV',
            data=csv_data,
            file_name='Instagram_Placeholder_Line_Chart_Data.csv',
            mime='text/csv'
        )


if input_media == ['Threads']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Threads
    st.subheader("Bar Chart - Total Followers Count for Threads")
    fig_th_bar = px.bar(thrd_data, x="Name (English)", y="Threads Follower #", title="Total Followers Count for Threads")
    st.plotly_chart(fig_th_bar)

    # Add a download button for the Bar Chart
    if st.button("Download Threads Bar Chart Data"):
        st.write("Downloading Threads Bar Chart Data...")
        csv_data = fig_th_bar.to_csv(index=False)
        st.download_button(
            label='Download Bar Chart Data as CSV',
            data=csv_data,
            file_name='Threads_Bar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 3: Donut Chart for Threads
    st.subheader("Donut Chart - Distribution of Followers for Threads")
    fig_th_donut = px.pie(thrd_data, names="Region of Focus", title="Distribution of Followers for Threads", hole=0.4)
    st.plotly_chart(fig_th_donut)

    # Add a download button for the Donut Chart
    if st.button("Download Threads Donut Chart Data"):
        st.write("Downloading Threads Donut Chart Data...")
        csv_data = fig_th_donut.to_csv(index=False)
        st.download_button(
            label='Download Donut Chart Data as CSV',
            data=csv_data,
            file_name='Threads_Donut_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 4: Radar Chart - Multidimensional Comparison for Threads
    st.subheader("Radar Chart - Multidimensional Comparison for Threads")
    fig_th_radar = px.line_polar(thrd_data, r="Threads Follower #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Threads")
    st.plotly_chart(fig_th_radar)

    # Add a download button for the Radar Chart
    if st.button("Download Threads Radar Chart Data"):
        st.write("Downloading Threads Radar Chart Data...")
        csv_data = fig_th_radar.to_csv(index=False)
        st.download_button(
            label='Download Radar Chart Data as CSV',
            data=csv_data,
            file_name='Threads_Radar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 5: Sunburst Chart - Proportional Representation for Threads
    st.subheader("Sunburst Chart - Proportional Representation for Threads")
    fig_th_sunburst = px.sunburst(thrd_data, path=["Region of Focus"], values="Threads Follower #", title="Proportional Representation of Follower Counts for Threads")
    st.plotly_chart(fig_th_sunburst)

    # Add a download button for the Sunburst Chart
    if st.button("Download Threads Sunburst Chart Data"):
        st.write("Downloading Threads Sunburst Chart Data...")
        csv_data = fig_th_sunburst.to_csv(index=False)
        st.download_button(
            label='Download Sunburst Chart Data as CSV',
            data=csv_data,
            file_name='Threads_Sunburst_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 7: Treemap - Proportional Representation of Total Followers for Threads
    st.subheader("Treemap - Proportional Representation of Total Followers for Threads")
    fig_th_treemap_total_followers = px.treemap(thrd_data, path=["Region of Focus", "Name (English)"], values="Threads Follower #",
                                                title="Proportional Representation of Total Followers by Region for Threads")
    st.plotly_chart(fig_th_treemap_total_followers)

    # Add a download button for the Treemap
    if st.button("Download Threads Treemap Data"):
        st.write("Downloading Threads Treemap Data...")
        csv_data = fig_th_treemap_total_followers.to_csv(index=False)
        st.download_button(
            label='Download Treemap Data as CSV',
            data=csv_data,
            file_name='Threads_Treemap_Data.csv',
            mime='text/csv'
        )

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatterth_global_distribution = px.scatter_3d(thrd_data, x="Region of Focus", y="Name (English)", z="Threads Follower #",
                                                    color="Threads Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatterth_global_distribution)

    # Add a download button for the 3D Scatter Plot
    if st.button("Download Threads 3D Scatter Plot Data"):
        st.write("Downloading Threads 3D Scatter Plot Data...")
        csv_data = fig_3d_scatterth_global_distribution.to_csv(index=False)
        st.download_button(
            label='Download 3D Scatter Plot Data as CSV',
            data=csv_data,
            file_name='Threads_3D_Scatter_Plot_Data.csv',
            mime='text/csv'
        )



elif input_media == ['Tiktok']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Tiktok
    st.subheader("Bar Chart - Total Followers Count for Tiktok")
    fig_tt_bar = px.bar(tiktok_data, x="Name (English)", y="TikTok Subscriber #", title="Total Followers Count for Tiktok")
    st.plotly_chart(fig_tt_bar)

    # Add a download button for the Bar Chart
    if st.button("Download Tiktok Bar Chart Data"):
        st.write("Downloading Tiktok Bar Chart Data...")
        csv_data = tiktok_data.to_csv(index=False)
        st.download_button(
            label='Download Bar Chart Data as CSV',
            data=csv_data,
            file_name='Tiktok_Bar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 3: Donut Chart for Tiktok
    st.subheader("Donut Chart - Distribution of Followers for Tiktok")
    fig_tt_donut = px.pie(tiktok_data, names="Region of Focus", title="Distribution of Followers for Tiktok", hole=0.4)
    st.plotly_chart(fig_tt_donut)

    # Add a download button for the Donut Chart
    if st.button("Download Tiktok Donut Chart Data"):
        st.write("Downloading Tiktok Donut Chart Data...")
        csv_data = tiktok_data.to_csv(index=False)
        st.download_button(
            label='Download Donut Chart Data as CSV',
            data=csv_data,
            file_name='Tiktok_Donut_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 4: Radar Chart - Multidimensional Comparison for Tiktok
    st.subheader("Radar Chart - Multidimensional Comparison for Tiktok")
    fig_tt_radar = px.line_polar(tiktok_data, r="TikTok Subscriber #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Tiktok")
    st.plotly_chart(fig_tt_radar)

    # Add a download button for the Radar Chart
    if st.button("Download Tiktok Radar Chart Data"):
        st.write("Downloading Tiktok Radar Chart Data...")
        csv_data = tiktok_data.to_csv(index=False)
        st.download_button(
            label='Download Radar Chart Data as CSV',
            data=csv_data,
            file_name='Tiktok_Radar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 5: Sunburst Chart - Proportional Representation for Tiktok
    st.subheader("Sunburst Chart - Proportional Representation for Tiktok")
    fig_tt_sunburst = px.sunburst(tiktok_data, path=["Region of Focus"], values="TikTok Subscriber #", title="Proportional Representation of Follower Counts for Tiktok")
    st.plotly_chart(fig_tt_sunburst)

    # Add a download button for the Sunburst Chart
    if st.button("Download Tiktok Sunburst Chart Data"):
        st.write("Downloading Tiktok Sunburst Chart Data...")
        csv_data = tiktok_data.to_csv(index=False)
        st.download_button(
            label='Download Sunburst Chart Data as CSV',
            data=csv_data,
            file_name='Tiktok_Sunburst_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 7: Treemap - Proportional Representation of Total Followers for Tiktok
    st.subheader("Treemap - Proportional Representation of Total Followers for Tiktok")
    fig_tt_treemap_total_followers = px.treemap(tiktok_data, path=["Region of Focus", "Name (English)"], values="TikTok Subscriber #",
                                                title="Proportional Representation of Total Followers by Region for Tiktok")
    st.plotly_chart(fig_tt_treemap_total_followers)

    # Add a download button for the Treemap
    if st.button("Download Tiktok Treemap Data"):
        st.write("Downloading Tiktok Treemap Data...")
        csv_data = tiktok_data.to_csv(index=False)
        st.download_button(
            label='Download Treemap Data as CSV',
            data=csv_data,
            file_name='Tiktok_Treemap_Data.csv',
            mime='text/csv'
        )

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scattertt_global_distribution = px.scatter_3d(tiktok_data, x="Region of Focus", y="Name (English)", z="TikTok Subscriber #",
                                                        color="TikTok Subscriber #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scattertt_global_distribution)

    # Add a download button for the 3D Scatter Plot
    if st.button("Download Tiktok 3D Scatter Plot Data"):
        st.write("Downloading Tiktok 3D Scatter Plot Data...")
        csv_data = tiktok_data.to_csv(index=False)
        st.download_button(
            label='Download 3D Scatter Plot Data as CSV',
            data=csv_data,
            file_name='Tiktok_3D_Scatter_Plot_Data.csv',
            mime='text/csv'
        )


elif input_media == ['Twitter']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Twitter
    st.subheader("Bar Chart - Total Followers Count for Twitter")
    fig_tw_bar = px.bar(twitter_data, x="Name (English)", y="X (Twitter) Follower #", title="Total Followers Count for Twitter")
    st.plotly_chart(fig_tw_bar)

    # Add a download button for the Bar Chart
    if st.button("Download Twitter Bar Chart Data"):
        st.write("Downloading Twitter Bar Chart Data...")
        csv_data = fig_tw_bar.to_csv(index=False)
        st.download_button(
            label='Download Bar Chart Data as CSV',
            data=csv_data,
            file_name='Twitter_Bar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 3: Donut Chart for Twitter
    st.subheader("Donut Chart - Distribution of Followers for Twitter")
    fig_tw_donut = px.pie(twitter_data, names="Region of Focus", title="Distribution of Followers for Twitter", hole=0.4)
    st.plotly_chart(fig_tw_donut)

    # Add a download button for the Donut Chart
    if st.button("Download Twitter Donut Chart Data"):
        st.write("Downloading Twitter Donut Chart Data...")
        csv_data = fig_tw_donut.to_csv(index=False)
        st.download_button(
            label='Download Donut Chart Data as CSV',
            data=csv_data,
            file_name='Twitter_Donut_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 4: Radar Chart - Multidimensional Comparison for Twitter
    st.subheader("Radar Chart - Multidimensional Comparison for Twitter")
    fig_tw_radar = px.line_polar(twitter_data, r="X (Twitter) Follower #", theta="Region of Focus", line_close=True, title="Twitter Count Multidimensional Comparison Twitter")
    st.plotly_chart(fig_tw_radar)

    # Add a download button for the Radar Chart
    if st.button("Download Twitter Radar Chart Data"):
        st.write("Downloading Twitter Radar Chart Data...")
        csv_data = fig_tw_radar.to_csv(index=False)
        st.download_button(
            label='Download Radar Chart Data as CSV',
            data=csv_data,
            file_name='Twitter_Radar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 5: Sunburst Chart - Proportional Representation for Twitter
    st.subheader("Sunburst Chart - Proportional Representation for Twitter")
    fig_tw_sunburst = px.sunburst(twitter_data, path=["Region of Focus"], values="X (Twitter) Follower #", title="Proportional Representation of Follower Counts for Twitter")
    st.plotly_chart(fig_tw_sunburst)

    # Add a download button for the Sunburst Chart
    if st.button("Download Twitter Sunburst Chart Data"):
        st.write("Downloading Twitter Sunburst Chart Data...")
        csv_data = fig_tw_sunburst.to_csv(index=False)
        st.download_button(
            label='Download Sunburst Chart Data as CSV',
            data=csv_data,
            file_name='Twitter_Sunburst_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 7: Treemap - Proportional Representation of Total Followers for Twitter
    st.subheader("Treemap - Proportional Representation of Total Followers for Twitter")
    fig_tw_treemap_total_followers = px.treemap(twitter_data, path=["Region of Focus", "Name (English)"], values="X (Twitter) Follower #",
                                                title="Proportional Representation of Total Followers by Region for Twitter")
    st.plotly_chart(fig_tw_treemap_total_followers)

    # Add a download button for the Treemap
    if st.button("Download Twitter Treemap Data"):
        st.write("Downloading Twitter Treemap Data...")
        csv_data = fig_tw_treemap_total_followers.to_csv(index=False)
        st.download_button(
            label='Download Treemap Data as CSV',
            data=csv_data,
            file_name='Twitter_Treemap_Data.csv',
            mime='text/csv'
        )

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scattertw_global_distribution = px.scatter_3d(twitter_data, x="Region of Focus", y="Name (English)", z="X (Twitter) Follower #",
                                                        color="X (Twitter) Follower #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scattertw_global_distribution)

    # Add a download button for the 3D Scatter Plot
    if st.button("Download Twitter 3D Scatter Plot Data"):
        st.write("Downloading Twitter 3D Scatter Plot Data...")
        csv_data = fig_3d_scattertw_global_distribution.to_csv(index=False)
        st.download_button(
            label='Download 3D Scatter Plot Data as CSV',
            data=csv_data,
            file_name='Twitter_3D_Scatter_Plot_Data.csv',
            mime='text/csv'
        )



elif input_media == ['Youtube']:
    # Streamlit app
    st.title("Social Media Presence Visualization")

    # Visualization 2: Bar Chart for Youtube
    st.subheader("Bar Chart - Total Followers Count for Youtube")
    fig_yt_bar = px.bar(yt_data, x="Name (English)", y="YouTube Subscriber #", title="Total Followers Count for Youtube")
    st.plotly_chart(fig_yt_bar)

    # Add a download button for the Bar Chart
    if st.button("Download Youtube Bar Chart Data"):
        st.write("Downloading Youtube Bar Chart Data...")
        csv_data = fig_yt_bar.to_csv(index=False)
        st.download_button(
            label='Download Bar Chart Data as CSV',
            data=csv_data,
            file_name='Youtube_Bar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 3: Donut Chart for Youtube
    st.subheader("Donut Chart - Distribution of Followers for Youtube")
    fig_yt_donut = px.pie(yt_data, names="Region of Focus", title="Distribution of Followers for Youtube", hole=0.4)
    st.plotly_chart(fig_yt_donut)

    # Add a download button for the Donut Chart
    if st.button("Download Youtube Donut Chart Data"):
        st.write("Downloading Youtube Donut Chart Data...")
        csv_data = fig_yt_donut.to_csv(index=False)
        st.download_button(
            label='Download Donut Chart Data as CSV',
            data=csv_data,
            file_name='Youtube_Donut_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 4: Radar Chart - Multidimensional Comparison for Youtube
    st.subheader("Radar Chart - Multidimensional Comparison for Youtube")
    fig_yt_radar = px.line_polar(yt_data, r="YouTube Subscriber #", theta="Region of Focus", line_close=True, title="Follower Count Multidimensional Comparison for Youtube")
    st.plotly_chart(fig_yt_radar)

    # Add a download button for the Radar Chart
    if st.button("Download Youtube Radar Chart Data"):
        st.write("Downloading Youtube Radar Chart Data...")
        csv_data = fig_yt_radar.to_csv(index=False)
        st.download_button(
            label='Download Radar Chart Data as CSV',
            data=csv_data,
            file_name='Youtube_Radar_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 5: Sunburst Chart - Proportional Representation for Youtube
    st.subheader("Sunburst Chart - Proportional Representation for Youtube")
    fig_yt_sunburst = px.sunburst(yt_data, path=["Region of Focus"], values="YouTube Subscriber #", title="Proportional Representation of Follower Counts for Youtube")
    st.plotly_chart(fig_yt_sunburst)

    # Add a download button for the Sunburst Chart
    if st.button("Download Youtube Sunburst Chart Data"):
        st.write("Downloading Youtube Sunburst Chart Data...")
        csv_data = fig_yt_sunburst.to_csv(index=False)
        st.download_button(
            label='Download Sunburst Chart Data as CSV',
            data=csv_data,
            file_name='Youtube_Sunburst_Chart_Data.csv',
            mime='text/csv'
        )

    # Visualization 7: Treemap - Proportional Representation of Total Followers for Youtube
    st.subheader("Treemap - Proportional Representation of Total Followers for Youtube")
    fig_yt_treemap_total_followers = px.treemap(yt_data, path=["Region of Focus", "Name (English)"], values="YouTube Subscriber #",
                                                title="Proportional Representation of Total Followers by Region for Youtube")
    st.plotly_chart(fig_yt_treemap_total_followers)

    # Add a download button for the Treemap
    if st.button("Download Youtube Treemap Data"):
        st.write("Downloading Youtube Treemap Data...")
        csv_data = fig_yt_treemap_total_followers.to_csv(index=False)
        st.download_button(
            label='Download Treemap Data as CSV',
            data=csv_data,
            file_name='Youtube_Treemap_Data.csv',
            mime='text/csv'
        )

    # Visualization 9: 3D Scatter Plot - Global Distribution of Followers
    st.subheader("3D Scatter Plot - Global Distribution of Followers")
    fig_3d_scatteryt_global_distribution = px.scatter_3d(yt_data, x="Region of Focus", y="Name (English)", z="YouTube Subscriber #",
                                                        color="YouTube Subscriber #", title="Global Distribution of Followers")
    st.plotly_chart(fig_3d_scatteryt_global_distribution)

    # Add a download button for the 3D Scatter Plot
    if st.button("Download Youtube 3D Scatter Plot Data"):
        st.write("Downloading Youtube 3D Scatter Plot Data...")
        csv_data = fig_3d_scatteryt_global_distribution.to_csv(index=False)
        st.download_button(
            label='Download 3D Scatter Plot Data as CSV',
            data=csv_data,
            file_name='Youtube_3D_Scatter_Plot_Data.csv',
            mime='text/csv'
        )
        



# Sample data (replace this with your own dataset)
data = pd.DataFrame({
    'Latitude': np.random.uniform(37.5, 37.7, 100),
    'Longitude': np.random.uniform(-122.5, -122.3, 100),
    'FollowerCount': np.random.randint(100, 10000, 100)
})

# Function to filter data based on user input
def filter_data(data, min_followers):
    return data[data['FollowerCount'] >= min_followers]

# Streamlit app
st.title("Streamlit App with Map")

# Sidebar for user input
min_followers = st.sidebar.slider("Minimum Followers", min_value=0, max_value=10000, value=1000)

# Filter data based on user input
filtered_data = filter_data(data, min_followers)

# Display the filtered data (for debugging purposes)
st.write("Filtered Data:")
st.write(filtered_data)

# Map visualization
st.subheader("Geographical Map - Followers Distribution")
map_data = filtered_data[['Latitude', 'Longitude', 'FollowerCount']]
folium_map = folium.Map(location=[filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()], zoom_start=12)
for index, row in map_data.iterrows():
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=5, color='blue', fill=True, fill_color='blue', fill_opacity=0.6).add_to(folium_map)

# Display the map
folium_static(folium_map)


# Feedback form
st.header("Provide Feedback")
feedback = st.text_area("Please share your feedback:")

# User information (optional)
user_name = st.text_input("Your Name (optional):")
user_email = st.text_input("Your Email (optional):")

# Submit feedback button
if st.button("Submit Feedback"):
    # Save feedback to a file, database, or perform any other desired action
    # In this example, let's just print the feedback to the console
    st.success("Feedback submitted successfully!")
    st.write("Feedback:", feedback)
    st.write("Name:", user_name)
    st.write("Email:", user_email)





#