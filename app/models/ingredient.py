from app.extensions import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sugars = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    fats = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    slng = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    other_solids = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    total_solid = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    pod = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    pac = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f'<Ingredient {self.name}>'