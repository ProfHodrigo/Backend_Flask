from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, Length

class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Enviar")

class ProdutoForm(FlaskForm):
    nome = StringField("Nome do Produto", validators=[DataRequired()])
    preco = FloatField("Preço", validators=[DataRequired(), NumberRange(min=0)])
    estoque = IntegerField("Estoque", validators=[NumberRange(min=0)])
    submit = SubmitField("Salvar")
