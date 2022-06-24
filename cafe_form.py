from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', description="Cafe Name", validators=[DataRequired()])
    location_url = StringField(label="Location URL", description="Copy / Paste location URL", validators=[DataRequired(), URL()])
    open = StringField(label="Open Time", description="EG: 10 AM", validators=[DataRequired()])
    close = StringField(label="Close Time ", description="EG: 8 PM", validators=[DataRequired()])
    coffee = SelectField(label="Coffee Rating", choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi = SelectField(label="Wifi Strength", choices=['❌', '📶📶', '📶📶📶', '📶📶📶📶', '📶📶📶📶📶'])
    power = SelectField(label="Power Availability", choices=['❌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label="Submit")

