from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe
import pytest

def test_returns_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")  
    repo = RecipeRepository(db_connection)
    

    recipes = repo.all()

    assert len(recipes) == 15
    assert recipes == [
        Recipe(1,'Spaghetti Carbonara', 25, 5),
        Recipe(2,'Chicken Tikka Masala', 45, 4),
        Recipe(3,'Beef Stroganoff', 40, 4),
        Recipe(4,'Miso Ramen', 50, 5),
        Recipe(5,'Shakshuka', 30, 4),
        Recipe(6,'Butternut Squash Soup', 35, 5),
        Recipe(7,'Pad Thai', 40, 4),
        Recipe(8,'Margherita Pizza', 20, 5),
        Recipe(9,'Falafel Wrap', 25, 4),
        Recipe(10,'Fish Tacos', 30, 4),
        Recipe(11,'Lasagna', 60, 5),
        Recipe(12,'Vegetable Stir Fry', 20, 3),
        Recipe(13,'Butter Chicken', 45, 5),
        Recipe(14,'Eggplant Parmesan', 50, 4),
        Recipe(15,'Chili con Carne', 55, 5)
    ]

def test_returns_a_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")  
    repo = RecipeRepository(db_connection)
    
    recipe = repo.find(1)

    assert recipe == Recipe(1,'Spaghetti Carbonara', 25, 5)

def test_raises_exception_for_non_existing_id(db_connection):
    db_connection.seed("seeds/music_library.sql") 
    repository = RecipeRepository(db_connection)
    with pytest.raises(Exception) as e:
        repository.find(16)

    assert str(e.value) == 'No such ID'