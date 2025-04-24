from lib.recipe import Recipe


class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["name"],
                          row["cooking_time"], row["rating"])
            recipes.append(item)
        return recipes
    
    def find(self, id):
        try:
            rows = self._connection.execute(
                'SELECT * from recipes WHERE id = %s', [id])
            recipe = Recipe(rows[0]["id"], rows[0]["name"],
                        rows[0]["cooking_time"], rows[0]["rating"])
            return recipe
        except IndexError:
            raise Exception("No such ID")