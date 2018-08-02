from scraping.validators.abstract_validator import AbstractValidator


class ProductValidator(AbstractValidator):

    def __init__(self):
        super().__init__()

    def schema(self):
        return {
                    'title': {'type': 'string', 'required': True, 'empty': False},
                    'price': {'type': 'float', 'required': True}
               }