spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names=[]
    for foods in spicy_foods:
         names.append(foods["name"])
    return names


def get_spiciest_foods(spicy_foods):
    spiciest_foods=[]
    for foods in spicy_foods:
        if foods["heat_level"] > 5:
            spiciest_foods.append(foods)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    chili= "🌶"
    for foods in spicy_foods:
        print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {foods['heat_level'] * chili}")

print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods["cuisine"] == cuisine:
            return foods  

def print_spiciest_foods(spicy_foods):
    chili= "🌶"
    for foods in spicy_foods:
        if foods["heat_level"] > 5:
            print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {foods['heat_level'] * chili}")
    

def get_average_heat_level(spicy_foods):
    spice=[]
    for foods in spicy_foods:
        spice.append(foods["heat_level"])
    return int(sum(spice)/3)
       
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
