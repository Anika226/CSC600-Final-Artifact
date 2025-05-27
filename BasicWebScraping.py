from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Create lists of the quotes and authors
quotes = soup.findAll("span", attrs = {"class": "text"})
authors = soup.findAll("small", attrs = {"class": "author"})

# Create csv file of webscraping results
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file) # writes them in a comma separated list
writer.writerow(["QUOTES", "AUTHORS"])

# Now loop through each quote and author in the lists
for quote, author in zip(quotes, authors):
    print(quote.text + "----" + author.text) 
    # Added for creating csv file
    writer.writerow([quote.text, author.text])
file.close()
    

# Simpler method of looping
# for quote in quotes: 
#     print(quote.text)
    
# for author in authors: 
#     print(author.text)