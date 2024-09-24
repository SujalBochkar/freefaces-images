
# Free Faces Gallery

A Streamlit web application that fetches and displays a collection of images from the Free Faces Gallery website. The images are fetched dynamically from the website and displayed in a grid format.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SujalBochkar/freefaces-images.git
   cd freefaces-images
   ```

2. **Install the required dependencies**:
   You can install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` should include the following packages:
   ```
   streamlit
   requests
   beautifulsoup4
   ```

3. **Run the application**:
   To run the Streamlit app, use the command:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   After running the command, open your browser and navigate to `http://localhost:8501` to view the application.

## Features

- **Image Scraping**: 
  - The app scrapes images from the Free Faces Gallery website.
  - Images are displayed in a responsive grid layout.
  
- **Pagination Support**: 
  - The app supports multiple pages of the Free Faces Gallery by dynamically fetching images from different page numbers.

## Usage

- **Image Display**: 
  The app scrapes images from multiple pages of the Free Faces Gallery and displays them in a grid format.
  
- **Responsive Layout**: 
  The images are arranged in a 3-column grid layout that adjusts according to the number of images fetched.

  
![image](https://github.com/user-attachments/assets/c1e020cc-b7d2-4350-bc14-44452099e9dc)

## Contribution

Feel free to submit pull requests for any improvements or new features.
