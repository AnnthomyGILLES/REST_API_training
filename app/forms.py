from wtforms import Form, IntegerField, SubmitField, validators, SelectField


class CalculForm(Form):
    """Create forms for Flask application integration"""
    first_number = IntegerField("First Number", [validators.DataRequired()])
    second_number = IntegerField("Second Number", [validators.DataRequired()])
    calculation = SelectField(u'Programming Language', choices=[('value_add', 'Add'), ('value_substract', 'Substract'),
                                           ('value_mult', 'Multiply'), ('value_divide', 'Divide')])
    submit = SubmitField("Submit")
