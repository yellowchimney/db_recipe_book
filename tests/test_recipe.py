from lib.recipe import Recipe

def test_recipe_attributes():
    recipe = Recipe(1, "Lasagna", 60, 5)

    assert recipe.id == 1
    assert recipe.title == "Lasagna"
    assert recipe.cooking_time == 60
    assert recipe.rating == 5

def test_recipe_returns_formatted_string():
    recipe = Recipe(1, "Lasagna", 60, 5)

    assert str(recipe) == "Recipe(1, Lasagna, 60, 5)"
    
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Lasagna", 60, 5)
    recipe2 = Recipe(1, "Lasagna", 60, 5)

    assert recipe1 == recipe2