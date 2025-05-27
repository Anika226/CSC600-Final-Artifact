# CSC600 Final Project: Recipe Suggestion Web App

For my final project for Dr. Zufelt's CSC600 Research and Development class, I created a working Streamlit web app that is locally hosted and allows users to input what ingredients they have in their kitchen, and then recieve recipe suggestions using the **Spoonacular API**. 

While this app is the primary deliverable, I also explored several topics throughout the term including:
- Web scraping/crawling
- Server-client interactions
- Prompt engineering
- API key exploration
- Denial of Service (DOS) and Distributed Denial of Service(DDOS) Attacks

**To get the full scope of my project and what I learned throughout the term, please read my 'CSC600_Final_Artifact_Journey.pdf' file.**

## How to run the app on your local device: 
1. Make sure you have Python (3.7+) and `pip` installed.
2. Install the required library: pip install -r requirements.txt
3. Open up the `Final Artifact` folder and ensure the following files are present: 
- `streamlitAPP.py`
- `api_utils.py`
- `requirements.txt`
4. **Open a terminal, navigate to the 'Final Artifact' folder, and run: streamlit run streamlitAPP.py**
5. The Streamlit app should open automatically in your browser. If it doesn’t, copy and paste the URL shown in your terminal (usually http://localhost:8501/).

## Other uploaded files

In addition to my main Streamlit webpage, I uploaded the following files which show my attempts at webscraping
- `BasicWebScraping.py` (successfully scrapes a webpage with quotes and authors, and returns results as a csv file in scraped_quotes.csv)
- `RecipeScraping.py` (includes my attempt at webscraping the 'Epicurious' recipe website)
