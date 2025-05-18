import json

# ---------- Ingredient Class ----------
class Ingredient:
    def __init__(self, name: str, tags: list[str]):
        self.name = name
        self.tags = tags

    def get_name(self) -> str:
        return self.name


# ---------- IngredientFactory Class ----------
class IngredientFactory:
    def __init__(self):
        self.ingredients: dict[str, Ingredient] = {}

    def get_ingredient(self, name: str) -> Ingredient:
        if name not in self.ingredients:
            self.ingredients[name] = Ingredient(name, [])
        return self.ingredients[name]


# ---------- Recipe Class ----------
class Recipe:
    def __init__(self, name: str, ingredients: list[Ingredient], steps: list[str], rating: float, is_favourite: bool):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.rating = rating
        self.is_favourite = is_favourite

    def display(self) -> str:
        ingredients_str = ', '.join([i.get_name() for i in self.ingredients])
        steps_str = '\n'.join([f"{i+1}. {s}" for i, s in enumerate(self.steps)])
        fav = "(Favourite)" if self.is_favourite else ""
        return f"Recipe: {self.name} {fav}\nIngredients: {ingredients_str}\nSteps:\n{steps_str}\nRating: {self.rating}/5"

    def update_rating(self, rating: float):
        self.rating = rating

    def toggle_favourite(self):
        self.is_favourite = not self.is_favourite

    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": [i.get_name() for i in self.ingredients],
            "steps": self.steps,
            "rating": self.rating,
            "is_favourite": self.is_favourite
        }


# ---------- RecipeBuilder Class ----------
class RecipeBuilder:
    def __init__(self):
        self.name = ""
        self.steps: list[str] = []
        self.ingredients: list[Ingredient] = []
        self.rating = 0.0
        self.is_favourite = False

    def add_name(self, name: str) -> str:
        self.name = name
        return self.name

    def add_step(self, step: str):
        self.steps.append(step)

    def add_ingredients(self, ingredients: list[Ingredient]) -> list[Ingredient]:
        self.ingredients = ingredients
        return self.ingredients

    def add_rating(self, rating: float) -> float:
        self.rating = rating
        return self.rating

    def toggle_favourite(self):
        self.is_favourite = not self.is_favourite

    def build(self) -> Recipe:
        return Recipe(
            name=self.name,
            ingredients=self.ingredients,
            steps=self.steps,
            rating=self.rating,
            is_favourite=self.is_favourite
        )


# ---------- Sorter Class ----------
class Sorter:
    @staticmethod
    def sort_name(recipes: list[Recipe]) -> list[Recipe]:
        return sorted(recipes, key=lambda r: r.name)

    @staticmethod
    def sort_rating(recipes: list[Recipe]) -> list[Recipe]:
        return sorted(recipes, key=lambda r: r.rating, reverse=True)

    @staticmethod
    def sort_random(recipes: list[Recipe]) -> list[Recipe]:
        import random
        random.shuffle(recipes)
        return recipes


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
                    ingredients=ingredients,
                    steps=entry["steps"],
                    rating=entry["rating"],
                    is_favourite=entry["is_favourite"]
                )
                self.recipes.append(recipe)
        except Exception as e:
            print(f"Failed to load recipes: {e}")

    def save_to_json(self, path: str):
        try:
            with open(path, 'w') as f:
                json.dump([r.to_dict() for r in self.recipes], f, indent=4)
        except Exception as e:
            print(f"Failed to save recipes: {e}")


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

        builder = RecipeBuilder()
        builder.add_name(name)
        builder.add_ingredients(ingredients)

        # Add steps one by one
        while True:
            step = self.get_input("Enter a cooking step (or type 'done' to finish): ")
            if step.lower() == 'done':
                break
            builder.add_step(step)

        rating = float(self.get_input("Enter rating (0-5): "))
        builder.add_rating(rating)

        favourite = self.get_input("Mark as favourite? (y/n): ").lower() == 'y'
        if favourite:
            builder.toggle_favourite()

        return builder.build()


# ---------- AppController Class ----------
class AppController:
    def __init__(self):
        self.manager = RecipeManager()
        self.ui = TerminalUI()
        self.recipe_file = "sample_recipes.json"
        self.manager.load_from_json(self.recipe_file)

    def run(self):
        while True:
            self.ui.show_menu()
            choice = self.ui.get_input("Choose an option: ")
            self.handle_input(choice)

    def handle_input(self, choice):
        if choice == '1':
            recipe = self.ui.prompt_for_recipe()
            self.manager.add_recipe(recipe)
            self.ui.display_message("Recipe added successfully!")
        elif choice == '2':
            name = self.ui.get_input("Enter recipe name to view: ")
            try:
                recipe = self.manager.get_recipe(name)
                self.ui.display_recipe(recipe)
            except ValueError as e:
                self.ui.display_message(str(e))
        elif choice == '3':
            selected = self.ui.display_recipe_names(self.manager.list_all())
            if selected:
                self.ui.display_recipe(selected)
        elif choice == '4':
            keyword = self.ui.get_input("Enter search keyword: ")
            results = self.manager.search(keyword)
            if not results:
                self.ui.display_message("No matches found. Showing favourite recipes instead:")
                results = self.manager.list_favourites()
            selected = self.ui.display_recipe_names(results)
            if selected:
                self.ui.display_recipe(selected)
        elif choice == '5':
            sorted_recipes = self.manager.sort_recipes().sort_name(self.manager.list_all())
            selected = self.ui.display_recipe_names(sorted_recipes)
            if selected:
                self.ui.display_recipe(selected)
        elif choice == '6':
            sorted_recipes = self.manager.sort_recipes().sort_rating(self.manager.list_all())
            selected = self.ui.display_recipe_names(sorted_recipes)
            if selected:
                self.ui.display_recipe(selected)
        elif choice == '7':
            name = self.ui.get_input("Enter recipe name to favourite: ")
            self.manager.favourite_recipe(name)
        elif choice == '8':
            name = self.ui.get_input("Enter recipe name to rate: ")
            rating = float(self.ui.get_input("Enter new rating (0-5): "))
            self.manager.rate_recipe(name, rating)
        elif choice == '9':
            favourites = self.manager.list_favourites()
            selected = self.ui.display_recipe_names(favourites)
            if selected:
                self.ui.display_recipe(selected)
        elif choice == '0':
            self.manager.save_to_json(self.recipe_file)
            self.ui.display_message("Recipes saved. Goodbye!")
            exit()
        else:
            self.ui.display_message("Invalid option. Please try again.")


# ---------- Entry Point ----------
if __name__ == "__main__":
    app = AppController()
    app.run()
