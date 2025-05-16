import Ingredient
import Recipe

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

