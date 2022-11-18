
# Сделать систему позволяющею подобрать рецепт по запросам пользователя и имеющимся продуктам, а также вести учет имеющихся продуктов. Пользователь начиная работать с системой может искать новый рецепт или же продолжить приготовление текущего рецепта. Если он выбирает новый рецепт, то система задает два вопроса: 1) готовим завтрак, обед или ужин; 2) какой один продукт должен быть обязательно в рецепте. Дальше система подбирает подходящий рецепт, на основе ответов на вопросы и имеющихся продуктов. И выдает список подходящих рецептов. Пользователь выбирает понравившийся рецепт и переходит в режим приготовления, в котором пошагово говориться какие и сколько надо взять продуктов и что с ними сделать. Также пользователь может просмотреть общий каталог рецептов. Выбрать понравившийся рецепт и посмотреть каких продуктов ему не хватает. После того как пользователь купил недостающие продукты, он вносит в систему какие продукты он купил.

class Product:
    """Класс продуктов - содержит название продукта"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class ProductsCatalog:
    """Класс каталога продуктов - содержит список продуктов (экземпляр класса Product)"""

    def __init__(self):
        self.products = []

    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def get_product_count(self):
        return len(self.products)

    def add_products(self, products):
        for product in products:
            self.add_product(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __str__(self):
        return '\n'.join([str(product) for product in self.products])


class UserProducts:
    """Класс продуктов - содержит продукты имеющие пользователь и методы: получить количество этих продуктов по названию, добавить продукт, удалить продукт"""

    def __init__(self):
        self.products = {}

    def get_product_count(self, product_name):
        return self.products.get(product_name, 0)

    def add_product(self, product_name, count):
        self.products[product_name] = self.get_product_count(
            product_name) + count

    def remove_product(self, product_name, count):
        self.products[product_name] = self.get_product_count(
            product_name) - count
        if self.products[product_name] <= 0:
            del self.products[product_name]

    def __str__(self):
        return '\n'.join([f'{product_name}: {count}' for product_name, count in self.products.items()])


class ProductAccounting:
    """Класс учета продуктов - позволяет вести учет имеющихся продуктов в классе ProductCatalog"""

    def __init__(self, products_catalog, user_products):
        self.products_catalog = products_catalog
        self.user_products = user_products

    def add_product_to_catalog(self, product_name, count):
        self.products_catalog.add_product(product_name, count)

    def remove_product_from_catalog(self, product_name, count):
        self.products_catalog.remove_product(product_name, count)

    def get_product_count_from_catalog(self, product_name):
        return self.user_products.get_product_count(product_name)

    def add_product_to_user(self, product_name, count):
        self.user_products.add_product(product_name, count)

    def remove_product_from_user(self, product_name, count):
        self.user_products.remove_product(product_name, count)

    def get_product_count_from_user(self, product_name):
        return self.user_products.get_product_count(product_name)

    def __str__(self):
        return '\n'.join([f'{product_name}: {count}' for product_name, count in self.user_products.products.items()])


class Recipe:
    """Класс рецептов - содержит название рецепта, продукты  для его приготовления"""

    def __init__(self, name, products, cooking_time, type, cooking_temperature):
        self.name = name
        self.cooking_time = cooking_time
        self.type = type
        self.cooking_temperature = cooking_temperature
        self.products = products

    def get_cooking_time(self):
        return self.cooking_time

    def get_type(self):
        return self.type

    def get_cooking_temperature(self):
        return self.cooking_temperature

    def get_products(self):
        return self.products

    def __str__(self):
        return f'{self.name}: {self.products}'


class RecipeCatalog:
    """Класс каталога рецептов - содержит список рецептов"""

    def __init__(self):
        self.recipes = []

    def get_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe

    def get_recipe_count(self):
        return len(self.recipes)

    def add_recipes(self, recipes):
        for recipe in recipes:
            self.add_recipe(recipe)

    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                self.recipes.remove(recipe)

    def __str__(self):
        return '\n'.join([str(recipe) for recipe in self.recipes])


class SearchRecipe:
    """Класс для поиска рецепта - позволяет искать рецепты по заданным параметрам"""

    def __init__(self, recipe_catalog):
        self.recipe_catalog = recipe_catalog

    def search_by_name(self, recipe_name):
        return self.recipe_catalog.get_recipe(recipe_name)

    def search_by_cooking_time(self, cooking_time):
        recipes = []
        for recipe in self.recipe_catalog.recipes:
            if recipe.get_cooking_time() == cooking_time:
                recipes.append(recipe)
        return recipes

    def search_by_type(self, type):
        recipes = []
        for recipe in self.recipe_catalog.recipes:
            if recipe.get_type() == type:
                recipes.append(recipe)
        return recipes

    def search_recipe_by_cooking_temperature(self, cooking_temperature):
        recipes = []
        for recipe in self.recipe_catalog.recipes:
            if recipe.get_cooking_temperature() == cooking_temperature:
                recipes.append(recipe)
        return recipes

    def search_by_products(self, products):
        recipes = []
        for recipe in self.recipe_catalog.recipes:
            if recipe.get_products() == products:
                recipes.append(recipe)
        return recipes

    def search_by_all_parameters(self, cooking_time, type, cooking_temperature, products):
        recipes = []
        for recipe in self.recipe_catalog.recipes:
            if recipe.get_cooking_time() == cooking_time and recipe.get_type() == type and recipe.get_cooking_temperature() == cooking_temperature and recipe.get_products() == products:
                recipes.append(recipe)
        return recipes

    def search_by_params(self, cooking_time=None, type=None, cooking_temperature=None, products=None):
        recipes = {}

        if cooking_time and type and cooking_temperature and products:
            return self.search_by_all_parameters(cooking_time, type, cooking_temperature, products)

        for recipe in self.recipe_catalog.recipes:
            rate = 0
            if cooking_time == recipe.get_cooking_time():
                rate += 1
            if type == recipe.get_type():
                rate += 1
            if cooking_temperature == recipe.get_cooking_temperature():
                rate += 1
            if products == recipe.get_products():
                rate += 1
            if rate > 1:
                recipes.append(recipe)
        return recipes


class RecipeStep:
    """Класс шага рецепта - содержит шаг приготовления рецепта"""

    def __init__(self, recipe):
        self.recipe = recipe
        self.step_description = []

    def add_step_description(self, step_description: list, amount):
        for i in range(amount):
            self.step_description.append(step_description[i])

    def get_step_description(self):
        return self.step_description

    def __str__(self):
        return '\n'.join([str(step) for step in self.step_description])


class CookingMode:
    """Класс режима приготовления - содержит режим симуляции приготовления еды по рецепту"""

    def __init__(self, recipe):
        self.recipe = recipe
        self.step = RecipeStep(self.recipe)

    def add_step_description(self, step_description: list, amount):
        self.step.add_step_description(step_description, amount)

    def get_step_description(self):
        return self.step.get_step_description()

    def __str__(self):
        return f'{self.recipe.name}: {self.step}'


class Questionnaire:
    """Класс для опросника - позволяет задать два вопроса: 1) готовим завтрак, обед или ужин; 2) какой один продукт должен быть обязательно в рецепте"""

    def __init__(self):
        self.question = ["готовим завтрак", "готовим обед", "готовим ужин"]

    def add_question(self, question):
        self.question.append(question)

    def get_question(self):
        return self.question


class Injector:
    """Класс Injector - содержит в себе все необходимые для работы приложения классы"""

    def __init__(self):
        self.recipe_catalog = RecipeCatalog()
        self.products = ProductsCatalog()
        self.questionnaire = Questionnaire()
        self.pick_up_recipe = PickUpRecipe(self.recipe_catalog, self.products)
        self.cooking_mode = CookingMode(self.recipe_catalog)

    def get_questionnaire(self):
        return self.questionnaire

    def show_pick_up_recipe(self):
        recipes = []
        for recipe in self.pick_up_recipe.pick_up_recipe():
            recipes.append(recipe)
        return recipes

    def show_cooking_mode(self):
        return self.cooking_mode

    def show_recipe(self):
        return self.recipe_catalog

    def show_products(self):
        return self.products


class Interface:
    """Класс Interface - содержит в себе все необходимые для работы приложения классы"""

    def __init__(self, injector):
        self.injector = injector
        self.questionnaire = self.injector.get_questionnaire()
        self.pick_up_recipe = self.injector.show_pick_up_recipe()
        self.cooking_mode = self.injector.show_cooking_mode()
        self.recipe_catalog = self.injector.show_recipe()
        self.products = self.injector.show_products()

    def show_questionnaire(self):
        for question in self.questionnaire.get_question():
            print(question)

    def menu(self):
        print("1. Подбор рецепта")
        print("2. Каталог рецептов")
        print("3. Каталог продуктов")
        print("4. Режим приготовления")
        print("5. Выход")
        print("Введите номер пункта меню: ")
        choice = input()
        if choice == "1":
            self.show_questionnaire()
        elif choice == "2":
            self.recipe_catalog
        elif choice == "3":
            self.products.show_products()
        elif choice == "4":
            self.cooking_mode.show_cooking_mode()
        elif choice == "5":
            exit()
        else:
            print("Неверный ввод")
            self.menu()


if __name__ == "__main__":
    injector = Injector()
    interface = Interface(injector)
    interface.menu()
