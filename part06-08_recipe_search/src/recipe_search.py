# Write your solution here
def search_by_name(filename: str, word: str):
    with open(filename) as file:
        lines = file.readlines()
        
    word = word.lower()
    recipes = []
    current_recipe = []
  
    for line in lines:
        line = line.strip()
        if line == "":
            if current_recipe:
                recipes.append(current_recipe)
                current_recipe = []
        else:
            current_recipe.append(line)
    
    if current_recipe:
        recipes.append(current_recipe)
    
    found_recipes = []
    for recipe in recipes:
        recipe_name = recipe[0]
        if word in recipe_name.lower():
            found_recipes.append(recipe_name)
    
    return found_recipes

# usage
found_recipes = search_by_name("recipes1.txt", "cake")

for recipe in found_recipes:
    print(recipe)