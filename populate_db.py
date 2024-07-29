from app import app, db
from app.models import Ingredient

def populate_db():
	ingredients = [
        Ingredient(name='Leite de Vaca', sugars=0.0, fats=3.0, slng=8.0, other_solids=2.0, total_solid=13.0, pod=1.0, pac=5.0),
        Ingredient(name='Sacarose', sugars=100.0, fats=0.0, slng=0.0, other_solids=0.0, total_solid=100.0, pod=100.0, pac=1.0),
	]

	db.session.bulk_save_objects(ingredients)
	db.session.commit()

if __name__ == '__main__':
	with app.app_context():
		populate_db()
		print("Database populated!")