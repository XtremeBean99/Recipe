# ---------- Ingredient Class ----------
class Ingredient:
    def __init__(self, name: str, tags: list[str]):
        self.name = name
        self.tags = tags

    def get_name(self) -> str:
        return self.name
