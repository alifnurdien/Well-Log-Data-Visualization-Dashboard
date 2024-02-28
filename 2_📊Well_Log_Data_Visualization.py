import pandas as pd
import plotly_express as px
import streamlit as st
import matplotlib.pyplot as plt

#link emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Welcome to Well Log Data Visualization",
                   page_icon = "🌏",
                   layout="wide"
)
#--mainpage--
st.title(":bar_chart: Well Log Data Visualization Dashboard")
st.markdown("##")
st.subheader("Welcome,")
st.markdown("This is a Well Log Data Visualization Dashboard, I'm glad that you are visiting this app. There are several visualization features that you can use here. Let's try it 🔥")
st.markdown("")
st.markdown("")
st.subheader("The Datasets of Well Log")


df = pd.read_excel(
    io = 'Data gabungan well_edit.xlsx',
    engine='openpyxl',
    sheet_name='Well',
    usecols='A:I',
    nrows=28789,
)


#--Sidebar--
st.sidebar.header("Filter The Data Here: ")
well_name = st.sidebar.multiselect(
    "Select the Well log data:",
    options=df["Well_Name"].unique(),
    default=df["Well_Name"].unique()
)
options = st.sidebar.radio("Visualization",options=['Line Plot','Scatter Plot','Histogram Plot','Box Plot','Violin Plot'])

df_selection = df.query(
    "Well_Name == @well_name"
)

st.dataframe(df_selection)

#--setting sidebar--&--Plotting visualization--
def line_plot (df_selection):
    x_axis_val = st.selectbox('Select X-Axis of Well Log Data', options=df_selection.columns)
    y_axis_val = st.selectbox('Select Y-Axis of Well Log Data', options=df_selection.columns)
    col1 =st.color_picker('Select your plot colour')

    plot = px.line(df_selection, x=x_axis_val,y=y_axis_val)
    plot.update_traces(line=dict(color=col1))
    plot.update_layout(title="Line Plot of Well Log Data")
    plot.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))
    st.plotly_chart(plot, use_container_width=True)

    
def scatter_plot (df_selection):
    x_axis_val = st.selectbox('Select X-Axis of Well Log Data', options=df_selection.columns)
    y_axis_val = st.selectbox('Select Y-Axis of Well Log Data', options=df_selection.columns)
    col =st.color_picker('Select your plot colour')

    plot = px.scatter(df_selection, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    plot.update_layout(title="Scatter Plot of Well Log Data")
    plot.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))
    st.plotly_chart(plot, use_container_width=True)


def histo_plot (df_selection):
    x_axis_val = st.selectbox('Select X-Axis Well Log Data', options=df_selection.columns)
    col =st.color_picker('Select your plot colour')

    plot = px.histogram(df_selection, x=x_axis_val)
    plot.update_traces(marker=dict(color=col))
    plot.update_layout(title="Histogram of Well Log Data", xaxis_title="Variable of Log",yaxis_title="Value")
    plot.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))
    st.plotly_chart(plot, use_container_width=True)

def box_plot (df_selection):
    y_axis_val = st.multiselect('Select Y-Axis of Well Log Data', options=df_selection.columns)
    col =st.color_picker('Select your plot colour')

    plot = px.box(df_selection, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    plot.update_layout(title="Box Plot of Well Log Data", xaxis_title="Variable of Log",yaxis_title="Value")
    plot.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))
    st.plotly_chart(plot, use_container_width=True)

def violin_plot (df_selection):
    y_axis_val = st.multiselect('Select Y-Axis of Well log data', options=df_selection.columns)
    col = st.color_picker('Select Your Colour Here:')

    plot = px.violin(df_selection,y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    plot.update_layout(title="Violin Plot of Well Log Data", xaxis_title="Variable of Log",yaxis_title="Value")
    plot.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))
    st.plotly_chart(plot, use_container_width=True)


if options == 'Line Plot':
    line_plot(df_selection)
elif options == 'Scatter Plot':
    scatter_plot(df_selection)
elif options == 'Histogram Plot':
    histo_plot(df_selection)
elif options == 'Box Plot':
    box_plot(df_selection)
elif options == 'Violin Plot':
    violin_plot(df_selection)

#-- hide streamlit origin style--
hide_st_style = """
            <style>
            #MainMenu (visibility: hidden;)
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
