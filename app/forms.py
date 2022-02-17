from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,EmailField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email("Поверьте адрес")])
    username = StringField('Имя пользователя', validators=[DataRequired("Укажите имя пользователя")])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')