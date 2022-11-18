# При покупке продуктов можно попросить систему заменить один продукт на другой. Система должна это учесть в дальнейшем
class ProductReplacement:
    """Класс замены продуктов - содержит список заменяемых продуктов"""

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog
        self.replacements = []

    def add_replacement(self, product_name, replacement_name):
        product = self.product_catalog.get_product(product_name)
        replacement = self.product_catalog.get_product(replacement_name)
        self.replacements.append((product, replacement))

    def get_replacement(self, product_name):
        product = self.product_catalog.get_product(product_name)
        for replacement in self.replacements:
            if replacement[0] == product:
                return replacement[1]

    def __str__(self):
        return '\n'.join([f'{replacement[0]} -> {replacement[1]}' for replacement in self.replacements])
