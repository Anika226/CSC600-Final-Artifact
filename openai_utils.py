# My Spoonacular API helper function for my streamlit recipe app
  
# Load OpenAI Python Package
import openai
# Helps interact with operating system; allows one to read environment vars like secret API key w/o hard-coding
import os
import requests

# Hardcoded spoonacular API key for testing
spoonacular_api_key = "16f1582c93324a469bf99f16bdfc48cc"

# Helper function to build spoonacular API request
def build_api_request(ingredients, number=5):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,
        "number": number,
        "apiKey": spoonacular_api_key
    }
    return url, params

# Helper function to format potentially recipes nicely
def format_recipe(idx, recipe):
    title = recipe['title']
    recipe_id = recipe['id']
    link = f"https://spoonacular.com/recipes/{title.replace(' ', '-').lower()}-{recipe_id}"

    used_ingredients = [ing['name'] for ing in recipe.get('usedIngredients', [])]
    used_ingredients_str = ", ".join(used_ingredients)

    formatted = f"**{idx}. [{title}]({link})**\n"
    
    # If any used ingredients are listed, show them under the title.
    if used_ingredients_str:
        formatted += f"_Uses: {used_ingredients_str}_\n"
    # Add blank line for spacing
    formatted += "\n"

    return formatted

# Main function that uses the helper functions to call the API and return formatted recipes
def recipe_suggestions(ingredients):
    # API URL + parameters
    url, params = build_api_request(ingredients)

    try:
        # Send GET request to the Spoonacular API.
        response = requests.get(url, params=params)
        
        # Check if the API call was successful (HTTP status code 200 means "OK")
        if response.status_code == 200:
            
            # Convert the API response JSON data into a Python list of recipes.
            recipes = response.json()
            if not recipes:
                return "No recipes found with these ingredients."

            result = ""
            for idx, recipe in enumerate(recipes, 1):
                result += format_recipe(idx, recipe)
            return result

        else:
            # If API call failed, return an error message.
            return "Error retrieving recipes. Please try again later."
        
    # Helps catch errors with code
    except Exception as e:
        return f"An error occurred: {e}"



# def recipe_suggestions(ingredients):
#     url = "https://api.spoonacular.com/recipes/findByIngredients"
#     params = {
#         "ingredients": ingredients,
#         "number": 2,
#         "apiKey": spoonacular_api_key
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         recipes = response.json()
#         if not recipes:
#             return "No recipes found with these ingredients."
#         result = ""
#         for recipe in recipes:
#             result += f"**{recipe['title']}**\nLink: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}\n\n"
#         return result
#     else:
#         return "Error retrieving recipes. Please try again later."

# ChatGPT API key code for workshopping later

# Set OpenAI API key (hardcoded for testing)

# # Functions that takes input of ingredients, and outputs recipe suggestions
# def recipe_suggestions(ingredients): 
#     # Builds prompt for ChatGPT
#     prompt = f"Give me 2 easy recipes using only these ingredients: {ingredients}. "
#     "For each recipe, include a title, a list of ingredients, and step-by-step cooking instructions. "
#     "Don't add any extra ingredients that aren't in the list."
#     # Sends prompt to ChatGPT
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = [{"role" : "user", "content" : prompt}],
#         # Sets max response length (300-350 words)
#         max_tokens = 400
#     )
#     # Returns response text from API which is orginially formatted as a dictionary 
#     return response.choices[0].message["content"]

    
