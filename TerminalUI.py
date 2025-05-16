from Recipe import Recipe
from Recipebuilder import Recipebuilder
from IngredientFactory import IngredientFactory

# ---------- TerminalUI Class ----------
class TerminalUI:
    def show_menu(self):
        print("""
        1. Add Recipe
        2. View Recipe
        3. View All Recipes
        4. Search Recipes
        5. Sort Recipes by Name
        6. Sort Recipes by Rating
        7. Favourite Recipe
        8. Rate Recipe
        9. List Favourites
        0. Exit
        """)

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def display_recipe(self, recipe: Recipe):
        print(recipe.display())

    def display_message(self, message: str):
        print(message)

    def display_recipe_names(self, recipes: list[Recipe]):
        if not recipes:
            self.display_message("No recipes found.")
            return None

        for idx, recipe in enumerate(recipes):
            print(f"{idx + 1}. {recipe.name}")

        choice = int(self.get_input("Select a recipe number to view or 0 to cancel: "))
        if choice == 0:
            return None
        return recipes[choice - 1]

    def prompt_for_recipe(self) -> Recipe:
        name = self.get_input("Enter recipe name: ")
        ing_names = self.get_input("Enter ingredients (comma-separated): ").split(',')
        factory = IngredientFactory()
        ingredients = [factory.get_ingredient(name.strip()) for name in ing_names]

        builder = Recipebuilder()
        builder.add_name(name)
        builder.add_ingredients(ingredients)

   
