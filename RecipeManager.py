# ---------- RecipeManager Class ----------
class RecipeManager:
    def __init__(self):
        self.recipes: list[Recipe] = []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def delete_recipe(self, name: str):
        self.recipes = [r for r in self.recipes if r.name != name]

    def edit_recipe(self, name: str, updated_recipe: Recipe):
        self.delete_recipe(name)
        self.recipes.append(updated_recipe)

    def get_recipe(self, name: str) -> Recipe:
        for r in self.recipes:
            if r.name == name:
                return r
        raise ValueError("Recipe not found")

    def sort_recipes(self) -> Sorter:
        return Sorter()

    def favourite_recipe(self, name: str):
        r = self.get_recipe(name)
        r.toggle_favourite()

    def rate_recipe(self, name: str, rating: float):
        r = self.get_recipe(name)
        r.update_rating(rating)

    def list_favourites(self) -> list[Recipe]:
        return [r for r in self.recipes if r.is_favourite]

    def search(self, keyword: str) -> list[Recipe]:
        return [r for r in self.recipes if keyword.lower() in r.name.lower()]

    def list_all(self) -> list[Recipe]:
        return self.recipes

    def load_from_json(self, path: str):
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            factory = IngredientFactory()
            for entry in data:
                ingredients = [factory.get_ingredient(i) for i in entry["ingredients"]]
                recipe = Recipe(
                    name=entry["name"],
