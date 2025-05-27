import streamlit as st
from openai_utils import recipe_suggestions
 
st.title("Welcome to RecipeMANIA!!")
st.write("Let's figure out how to use up those ingredients in your kitchen!")

# Initialize the ingredients list if it doesn't already exist
st.session_state.setdefault('ingredients', [])

# Function to add the ingredient and clear the input box
def add_ingredient():
    ingredient = st.session_state["ingredient_input"].strip()
    if ingredient:
        st.session_state.ingredients.append(ingredient)
        st.session_state["ingredient_input"] = ""  # Clear the input after adding
    else:
        st.warning("Please enter a valid ingredient.")

# Input box for ingredients; pressing Enter will trigger add_ingredient
st.text_input(
    "Enter an ingredient:",
    key="ingredient_input",
    on_change=add_ingredient
)

# Display the current list of ingredients with remove buttons
st.markdown("#### Ingredients List:")

if st.session_state.ingredients:
    for idx, ingredient in enumerate(st.session_state.ingredients):
        col1, col2 = st.columns([4, 1])  # One column for text, one for the remove button
        with col1:
            st.markdown(f"<span style='color: green;'>- {ingredient}</span>", unsafe_allow_html=True)
        with col2:
            if st.button("Remove", key=f"remove_{idx}"):
                st.session_state.ingredients.pop(idx)
                st.experimental_rerun()  # Refresh to immediately show the updated list
else:
    st.info("No ingredients added yet!")

# When the user clicks Find Recipes, call the recipe function
if st.button("Find Recipes"):
    if not st.session_state.ingredients:
        st.warning("Add at least one ingredient before searching!")
    else:
        ingredients_str = ", ".join(st.session_state.ingredients)
        recipes = recipe_suggestions(ingredients_str)
        st.markdown("### Suggested Recipes:")
        st.markdown(recipes, unsafe_allow_html=True)



# # Simpler Version of UI: 

# # Input text
# ingredients_inp = st.text_area("Please enter the ingredients you have in your kitchen (separated by commas):")

# # Waits for user to click "Find Recipes" button 
# if st.button("Find Recipes: "):
#     # Display ingredients user entered
#     st.write("You entered: ")
    
#     # Create list of ingredients user has
#     ingredients = []
    
#     for ingredient in ingredients_inp.split(","): 
#         ingredient = ingredient.strip()
#         # Make sure it's not empty
#         if ingredient != "":
#             ingredients.append(ingredient)
            
#     # Display cleaned list of ingredients
#     st.write(ingredients)
    
#     # Call the OpenAI function + displays potential recipes nicely
#     recipes = recipe_suggestions(", ".join(ingredients))
#     st.markdown("### Potential Recipes:")
#     st.write(recipes)
    
    
    