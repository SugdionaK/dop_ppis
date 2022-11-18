# Система при выборе нового рецепта задает дополнительный вопрос: на скольких человек готовим. Ответ учитывается при приготовлении
class QuestionnaireForNewRecipe(Questionnaire):
    """Класс для опросника - позволяет задать два вопроса: 1) готовим завтрак, обед или ужин; 2) какой один продукт должен быть обязательно в рецепте"""

    def __init__(self):
        super().__init__()
        self.question.append("на скольких человек готовим")

    def add_question(self, question):
        self.question.append(question)

    def get_question(self):
        return self.question