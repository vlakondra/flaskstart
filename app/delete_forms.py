from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,EmailField,FileField
from wtforms.validators import DataRequired,Email,Length

class LoginForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email("Проверьте адрес")])
    username = StringField('Имя пользователя', render_kw={"class":"input"} , validators=[DataRequired("Укажите имя пользователя")],description="qwe")
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')