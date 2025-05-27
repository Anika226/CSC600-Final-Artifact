from bs4 import BeautifulSoup
import requests
import csv
import time 
  
base_url = "https://www.epicurious.com/"
# categories = ["breakfast", "lunch", "dinner"]

# Breakfast category
search_url = "https://www.epicurious.com/recipes-menus/best-breakfast-recipes-gallery"


# Scrape and create lists of the titles, inredients, and urls

# Request + parse the page
page = requests.get(search_url)
soup = BeautifulSoup(search_url.text, "html.parser")

# Collect recipe links (via recipe cards and <a> tags)
recipe_cards = soup.find_all("a", class_="view-complete-item")

# Collect titles, ingredients, URLs
titles = []
ingredients_list = []
recipe_links = []

for card in recipe_cards:
    # Collect URLs via the href attribute
    href = card.get('href')        
    if href and href.startswith("/recipes"):  
        full_url = base_url + href  
        recipe_links.append(full_url) # FINISH THIS FIGURE OUT HOW THE URLs ARE FORMATTED (incorrect rn)
        
# Scrape each recipe page
for link in recipe_links:
    recipe_page = requests.get(link)
    recipe_soup = BeautifulSoup(recipe_page.text, "html.parser")

    # Title
    title_tag = recipe_soup.find("h1", class_="title-source")
    title = title_tag.text.strip() if title_tag else "N/A"
    titles.append(title)

    # Ingredients
    ingredient_tags = recipe_soup.find_all("li", class_="ingredient")
    ingredients = [i.text.strip() for i in ingredient_tags]
    ingredients_joined = "; ".join(ingredients)
    ingredients_list.append(ingredients_joined)    

