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
