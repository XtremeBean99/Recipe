from Recipe import Recipe
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

