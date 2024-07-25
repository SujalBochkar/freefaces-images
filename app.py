import requests
from bs4 import BeautifulSoup
import streamlit as st

image_links = []
for i in range(1, 10):
    link = f"https://www.freefaces.gallery/?3a2d1f52_page={i}"
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    a_tag = soup.find_all("a", class_="item-link")
    for a in a_tag:
        image_links.append(a.get("style")[22:-2])
len(image_links)

num_images = len(image_links)
num_rows = (num_images + 2) // 3


for i in range(num_rows):

    col1, col2, col3 = st.columns(3)

    with col1:
        index = i * 3
        if index < num_images:
            st.image(image_links[index], use_column_width=True)

    with col2:
        index = i * 3 + 1
        if index < num_images:
            st.image(image_links[index], use_column_width=True)

    with col3:
        index = i * 3 + 2
        if index < num_images:
            st.image(image_links[index], use_column_width=True)
