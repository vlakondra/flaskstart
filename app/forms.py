from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired,InputRequired,EqualTo,Length
# from  wtforms import validators

class RegForm(FlaskForm):
    name = StringField('Имя',   
                        validators=[ DataRequired(), Length(min=8)],
                        render_kw={'class':"input is-success",
                        'placeholder':"Имя пользователя",
                        'style':'margin-top:0px'}
                        )

    password = PasswordField('Пароль',
                             [InputRequired(), 
                             EqualTo('confirm', message='пароли не совпадают')],
                             render_kw={'class':"input is-success", 
                             'placeholder':"введите пароль"},
                            )
   
   
    confirm  = PasswordField('Повторите пароль' ,
                              render_kw={'class':"input is-success",
                              'placeholder':"повторите пароль",
                              'style':'margin-top:0px'} 
                            ) 


class CheckForm(FlaskForm):
    # chk = FieldList(BooleanField('check')) 
    chk = BooleanField('check')                    
