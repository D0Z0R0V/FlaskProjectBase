from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired 


class SiteForm(FlaskForm):
    username = StringField("", validators=[Length(min=5, max=30), InputRequired()])
    password = PasswordField("", validators=[Length(min=8, max=24), InputRequired()])
    about_me = TextAreaField("")
    submit = SubmitField("")
