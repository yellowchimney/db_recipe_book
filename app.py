from lib.db_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

conn = DatabaseConnection()
conn.connect()
conn.seed('seeds/recipes.sql')

recipe_repo = RecipeRepository(conn)

recipes = recipe_repo.all()

for recipe in recipes:
    print(recipe)