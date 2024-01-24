import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web Scraper", page_icon=":globe_with_meridians:", layout="wide")

st.markdown("<h1> Web Scraper </h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keywird")
    search = st.form_submit_button("Search")
    
placeholder = st.empty()

if search and keyword != "": 
    col1, col2 = placeholder.columns(2)
    
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_ = "ripi6")
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img", class_="a5VGX")
            listImg=img['srcset'].split("?")
            anchor = figures[i].find("a")
            
            if i == 0:
                col1.image(listImg[0])
                btn = col1.button("Download", key=str(index)+str(i))
                if btn: 
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
            else:
                col2.image(listImg[0])
                btn = col2.button("Download", key=str(index)+str(i))
                if btn: 
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
