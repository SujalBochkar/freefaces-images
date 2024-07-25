import requests
from bs4 import BeautifulSoup
import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Free Faces Gallery", layout="wide")

# Add a title and description
st.title("Free Faces Gallery")
st.markdown(
    """
    Welcome to the Free Faces Gallery! This app fetches and displays a collection of images from the Free Faces Gallery website.
    Each page of the gallery is checked, and images are displayed in a grid format.
    """
)

# Add a loading spinner
with st.spinner("Fetching images, please wait..."):
    image_links = []
    for i in range(1, 10):
        link = f"https://www.freefaces.gallery/?3a2d1f52_page={i}"
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")
        a_tags = soup.find_all("a", class_="item-link")
        for a in a_tags:
            # Extract the image URL from the style attribute
            img_url = a.get("style")[22:-2]
            if img_url:
                image_links.append(img_url)

    num_images = len(image_links)

# Show a message if no images were found
if num_images == 0:
    st.warning("No images were found. Please try again later.")
else:
    st.success(f"Found {num_images} images!")

    # Display images in a grid layout
    num_rows = (num_images + 2) // 3
    st.subheader("Image Gallery")

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

