from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange

class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    submit = SubmitField("Enviar")

class ProdutoForm(FlaskForm):
    nome = StringField("Nome do Produto", validators=[DataRequired()])
    preco = FloatField("Preço", validators=[DataRequired(), NumberRange(min=0)])
    estoque = IntegerField("Estoque", validators=[NumberRange(min=0)])
    submit = SubmitField("Salvar")
