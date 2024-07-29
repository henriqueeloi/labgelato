from app.extensions import db
from app.models.ingredient import Ingredient

class IngredientService():
    def get_all_ingredients(self):
        return Ingredient.query.all()

    def get_ingredient_by_id(self, ingredient_id):
        return Ingredient.query.get(ingredient_id)

    def create_ingredient(self, ingredient):
        if not ingredient:
            return None
        if ingredient.fats > 15.0:
            raise ValueError('O total de açúcares não pode ser maior que 15g')
        
        db.session.add(ingredient)
        db.session.commit()
        return ingredient

    def update_ingredient(self, ingredient_id, name):
        ingredient = Ingredient.query.get(ingredient_id)
        ingredient.name = name
        db.session.commit()
        return ingredient

    def delete_ingredient(self, ingredient_id):
        ingredient = Ingredient.query.get(ingredient_id)
        db.session.delete(ingredient)
        db.session.commit()
        return