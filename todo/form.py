from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired 


class SiteForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[Length(min=5, max=30), InputRequired()])
    password = PasswordField("Пароль", validators=[Length(min=8, max=24), InputRequired()])
    submit = SubmitField("Принять")
