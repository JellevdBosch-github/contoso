from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, PasswordField, BooleanField, SubmitField, ValidationError, \
    DateField, RadioField
from wtforms.validators import *


class CreateProduct(FlaskForm):
    name = StringField('Product name', validators=[InputRequired(), Length(3, 50)])
    description = StringField('Product description', validators=[InputRequired(), Length(3, 50)])
    type = StringField('Product type', validators=[InputRequired(), Length(3, 50)])
    manufacturer = StringField('Product manufacturer', validators=[InputRequired(), Length(3, 50)])
    brand_name = StringField('Product brand name', validators=[InputRequired(), Length(3, 20)])
    color = StringField('Product color', validators=[InputRequired(), Length(3, 20)])
    size = StringField('Product size', validators=[InputRequired(), Length(3, 50)])
    weight = StringField('Product weight', validators=[InputRequired(), Length(1, 6)])
    size_unit_measurement = StringField('Product size_unit_measurement', validators=[InputRequired(), Length(3, 20)])
    weight_unit_measurement = StringField('Product size_unit_measurement', validators=[InputRequired(), Length(3, 40)])
    cost = StringField('Product cost', validators=[InputRequired(), Length(3, 6)])
    price = StringField('Product price', validators=[InputRequired(), Length(3, 6)])
    status = StringField('Product status', validators=[InputRequired(), Length(3, 25)])
    category_name = StringField('Product category name', validators=[InputRequired(), Length(3, 50)])
    submit_create_product = SubmitField("Add")


class CreateCategory(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(3, 50)])
    description = StringField('description', validators=[InputRequired(), Length(3, 50)])
    submit_create_cat = SubmitField("Add")
