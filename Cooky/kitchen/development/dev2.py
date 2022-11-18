# В процессе приготовление может поменяться количество порций, система должна сказать, что нужно добавить в зависимости от выполненных шагов
class CookingModeWithChangePortion(CookingMode):
    """Класс режима приготовления с изменением количества порций - содержит режим симуляции приготовления еды по рецепту с изменением количества порций"""

    def __init__(self, recipe):
        super().__init__(recipe)
        self.portion = recipe.portion

    def add_step_description(self, step_description: list, amount):
        self.step.add_step_description(step_description, amount)
        self.portion += 1

    def get_step_description(self):
        return self.step.get_step_description()

    def __str__(self):
        return f'{self.recipe.name}: {self.step}'
