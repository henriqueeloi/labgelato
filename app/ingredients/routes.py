from flask import jsonify, render_template, request, flash, redirect, url_for

from app.ingredients import bp
from app.models.ingredient import Ingredient

from .services import IngredientService


@bp.route('/')
def index():
    ingredients = Ingredient.query.all()
    return render_template('ingredients/index.html', ingredients=ingredients)

@bp.route('/<int:ingredient_id>')
def ingredient(ingredient_id):
    ingredient = [Ingredient.query.get_or_404(ingredient_id)]
    return render_template('ingredients/index.html', ingredients=ingredient)

@bp.route('/create', methods=['GET', 'POST'])
def create_ingredient():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        sugars = float(data.get('sugars'))
        fats = float(data.get('fats'))
        slng = float(data.get('slng'))
        other_solids = float(data.get('other_solids'))
        pod = float(data.get('pod'))
        pac = float(data.get('pac'))

        new_ingredient = Ingredient(name=name, sugars=sugars, fats=fats, slng=slng, other_solids=other_solids, pod=pod, pac=pac)

        try:
            ingredient = IngredientService().create_ingredient(new_ingredient)
            flash('Ingredient created successfully!', 'success')
            return redirect(url_for('ingredients.index'))
        except ValueError as e:
            flash(str(e), 'error')
            return render_template('ingredients/create.html', data=data)
        
    return render_template('ingredients/create.html')

@bp.route('/categories/')
def categories():
    return render_template('ingredients/categories.html')