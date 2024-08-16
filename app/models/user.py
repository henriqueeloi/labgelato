from app.extensions import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	created_at = db.Column(db.DateTime, server_default=db.func.now())

	# Relacionamento um-para-muitos com RecipeVersion
	recipe_versions = db.relationship('RecipeVersion', backref='user', lazy=True)

	def __repr__(self):
		return f'<User {self.username}>'