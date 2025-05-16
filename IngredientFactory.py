# ---------- IngredientFactory Class ----------
class IngredientFactory:
    def __init__(self):
        self.ingredients: dict[str, Ingredient] = {}

    def get_ingredient(self, name: str) -> Ingredient:
        if name not in self.ingredients:
            self.ingredients[name] = Ingredient(name, [])
        return self.ingredients[name]
