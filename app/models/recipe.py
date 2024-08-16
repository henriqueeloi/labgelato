from app.extensions import db

# Tabela associativa para relacionar receitas e ingredientes
recipe_ingredient = db.Table('recipe_ingredient',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True),
    db.Column('quantity_grams', db.Float, nullable=False)
)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relacionamento muitos-para-muitos com Ingredient
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredient, backref=db.backref('recipes', lazy=True))

    def __repr__(self):
        return f'<Recipe {self.name}>'