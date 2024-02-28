import pandas as pd
import plotly_express as px
import streamlit as st


#link emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Welcome to Well Log Data Visualization",
                   page_icon = "🌏",
                   layout="wide"
)
#--mainpage--
st.title(" 📃 Homepage of Well Log Data Visualization Dashboard")
st.markdown("##")
st.subheader("👋 Hi there!")
st.markdown('<div style="text-align: justify;"> Welcome to this page, let me introduce myself. I\'m Alif, I\'m learning to make a dashboard application in Streamlit. This dashboard is a visualization application for well log data and there are several visualization features that you can try. It should be noted that the data used is original data and has not been subjected to any treatment (e.g Normalization, Outlier Cleaning, Missing Value, etc). The dataset used is a free access dataset which you can also access at the link below. </div>', unsafe_allow_html=True)
st.markdown("Let's go to the next page to explore the visualization 🔥")
st.markdown("")
st.markdown("Link of the dataset :https://terranubis.com/datainfo/NW-Shelf-Australia-Poseidon-3D ")

#-- hide streamlit origin style--
hide_st_style = """
            <style>
            #MainMenu (visibility: hidden;)
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

