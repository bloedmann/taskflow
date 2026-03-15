from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


# Formular für Aufgaben
class TaskForm(FlaskForm):
    title = StringField("Aufgabe", validators=[DataRequired(), Length(min=1, max=150)])
    priority = SelectField(
        "Priorität",
        choices=[
            ("niedrig", "Niedrig"),
            ("mittel", "Mittel"),
            ("hoch", "Hoch"),
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField("Speichern")
