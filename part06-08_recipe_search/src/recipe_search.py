# write your solution here
def read_recipes(filename):
    with open(filename) as file:
        lines = file.readlines()
        
    recipes = []
    current_recipe = {}
    ingredients = []
  
    for line in lines:
        line = line.strip()
        if not line:
            if current_recipe:
                current_recipe['ingredients'] = ingredients
                recipes.append(current_recipe)
                current_recipe = {}
                ingredients = []
        elif 'name' not in current_recipe:
            current_recipe['name'] = line
        elif 'prep_time' not in current_recipe:
            current_recipe['prep_time'] = int(line)
        else:
            ingredients.append(line)
    
    if current_recipe:
        current_recipe['ingredients'] = ingredients
        recipes.append(current_recipe)
    
    return recipes

def search_by_name(filename, word):
    recipes = read_recipes(filename)
    word = word.lower()
    found_recipes = [recipe['name'] for recipe in recipes if word in recipe['name'].lower()]
    return found_recipes

def search_by_time(filename, prep_time):
    recipes = read_recipes(filename)
    found_recipes = [f"{recipe['name']}, preparation time {recipe['prep_time']} min" for recipe in recipes if recipe['prep_time'] <= prep_time]
    return found_recipes

def search_by_ingredient(filename, ingredient):
    recipes = read_recipes(filename)
    ingredient = ingredient.lower()
    found_recipes = [f"{recipe['name']}, preparation time {recipe['prep_time']} min" for recipe in recipes if any(ingredient in ing.lower() for ing in recipe['ingredients'])]
    return found_recipes