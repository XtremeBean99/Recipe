import RecipeManager
import TerminalUI

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
