from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, FloatField,\
    DateTimeField, BooleanField, IntegerField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Optional
from models import Pool, GroupPool, MovementReason

from wtforms import DateTimeField
from datetime import datetime, timedelta


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class PoolForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    square = FloatField('Площадь', validators=[Optional()])
    deep = FloatField('Глубина', validators=[Optional()])
    submit = SubmitField('Сохранить')

class GroupPoolForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    pools = SelectMultipleField('Состоит из бассейнов', coerce=int, option_widget=BooleanField())
    submit = SubmitField('Сохранить')

    def __init__(self, *args, **kwargs):
        super(GroupPoolForm, self).__init__(*args, **kwargs)
        self.pools.choices = [(pool.id, pool.name) for pool in Pool.query.all()]

class HydrochemistryFilterForm(FlaskForm):
    start_date = DateTimeField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    end_date = DateTimeField('Конечная дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Фильтр')

class HydrochemistryGraphForm(FlaskForm):
    parameter = SelectField('Параметр', choices=[
        ('doxy', 'Кислород'),
        ('temperature', 'Температура'),
        ('ph', 'pH'),
        ('no2', 'NO2'),
        ('no3', 'NO3'),
        ('nh4', 'NH4'),
        ('po4', 'PO4'),
        ('salinity', 'Соленость'),
        ('illumination', 'Освещенность')
    ], validators=[DataRequired()])
    start_date = DateField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('Конечная дата', default=datetime.utcnow() + timedelta(days=1), format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Отобразить')

class HydrochemistryForm(FlaskForm):
    group_pool_id = SelectField('Групповой бассейн', coerce=int, validators=[DataRequired()])
    hydrochem_date = DateTimeField('Дата', default=datetime.utcnow, format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    doxy = FloatField('Doxy', validators=[Optional()])
    temperature = FloatField('Темпер.', validators=[Optional()])
    ph = FloatField('Ph', validators=[Optional()])
    no2 = FloatField('NO2', validators=[Optional()])
    no3 = FloatField('NO3', validators=[Optional()]) # NumberRange(0, 10, 'Rating should be from 0 to 10')
    nh4 = FloatField('NH4', validators=[Optional()])
    po4 = FloatField('PO4', validators=[Optional()])
    salinity = FloatField('Солен.', validators=[Optional()])
    illumination = FloatField('Освещ.', validators=[Optional()])
    submit = SubmitField('Сохранить')

    def __init__(self, *args, **kwargs):
        super(HydrochemistryForm, self).__init__(*args, **kwargs)
        self.group_pool_id.choices = [(gp.id, gp.name) for gp in GroupPool.query.all()]

# Форма для FishType
class FishTypeForm(FlaskForm):
    name = StringField('Вид рыбы', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class FishInventoryFilterForm(FlaskForm):
    start_date = DateTimeField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    end_date = DateTimeField('Конечная дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Фильтр')

# Форма для FishInventory
class FishInventoryForm(FlaskForm):
    control_date = DateTimeField('Дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    pool_id = SelectField('Бассейн', coerce=int, validators=[DataRequired()])
    fish_type_id = SelectField('Вид рыбы', coerce=int, validators=[DataRequired()])
    control_desc = TextAreaField('Описание', validators=[Optional()])
    submit = SubmitField('Сохранить')

# Форма для FishBoning
class FishBoningForm(FlaskForm):
    fish_inventory_id = SelectField('Идентификатор', coerce=int, validators=[DataRequired()])
    fish_number = IntegerField('Количество', validators=[DataRequired()])
    fish_biomass = FloatField('Биомасса', validators=[DataRequired()])
    fish_survival = FloatField('Выживаемость', validators=[Optional()])
    fish_biometric = TextAreaField('Биометрические показания', validators=[Optional()])
    fish_comment = TextAreaField('Комментарий', validators=[Optional()])
    submit = SubmitField('Сохранить')

class FeedTypeForm(FlaskForm):
    name = StringField('Тип корма', validators=[DataRequired()])
    unit = StringField('Тип единицы', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class FeedFilterForm(FlaskForm):
    start_date = DateTimeField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    end_date = DateTimeField('Конечная дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Фильтр')

class FeedForm(FlaskForm):
    pool_id = SelectField('Бассейн', coerce=int, validators=[DataRequired()])
    feed_date = DateTimeField('Дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    feed_type_id = SelectField('Тип корма', coerce=int, validators=[DataRequired()])
    feed_value = FloatField('Объем', validators=[DataRequired()])
    feed_desc = TextAreaField('Описание', validators=[Optional()])
    submit = SubmitField('Сохранить')

'''
class FishMovementFilterForm(FlaskForm):
    start_date = DateTimeField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    end_date = DateTimeField('Конечная дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Фильтр')

class FishMovementForm(FlaskForm):
    pool_id_from = SelectField('Откуда (бассейн)', coerce=int, validators=[Optional()])
    pool_id_to = SelectField('Куда (бассейн)', coerce=int, validators=[Optional()])
    fish_type_id = SelectField('Вид рыбы', coerce=int, validators=[DataRequired()])
    movement_date = DateTimeField('Дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    fish_biomass = FloatField('Биомасса', validators=[DataRequired()])
    movement_reason = TextAreaField('Причина перемещения', validators=[Optional()])
    movement_desc = TextAreaField('Описание', validators=[Optional()])
    submit = SubmitField('Сохранить')
'''

class FishMovementFilterForm(FlaskForm):
    start_date = DateTimeField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    end_date = DateTimeField('Конечная дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    movement_reason = SelectField('Причина перемещения', choices=[('', 'Все')] + [(reason.name, reason.value) for reason in MovementReason], validators=[Optional()])
    submit = SubmitField('Фильтр')

class FishMovementForm(FlaskForm):
    pool_id_from = SelectField('Откуда (бассейн)', coerce=int, validators=[Optional()])
    pool_id_to = SelectField('Куда (бассейн)', coerce=int, validators=[Optional()])
    fish_type_id = SelectField('Вид рыбы', coerce=int, validators=[DataRequired()])
    movement_date = DateTimeField('Дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    fish_biomass = FloatField('Биомасса', validators=[DataRequired()])
    movement_reason = SelectField('Причина перемещения',
                                  choices=[(reason.name, reason.value) for reason in MovementReason],
                                  validators=[DataRequired()])
    movement_desc = TextAreaField('Описание', validators=[Optional()])
    submit = SubmitField('Сохранить')

class PoolSelectionForm(FlaskForm):
    pool_id = SelectField('Бассейн', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Отобразить')

    def __init__(self, *args, **kwargs):
        super(PoolSelectionForm, self).__init__(*args, **kwargs)
        self.pool_id.choices = [(pool.id, pool.name) for pool in Pool.query.all()]

class FishInventoryAndBoningForm(FlaskForm):
    control_date = DateTimeField('Дата', default=datetime.utcnow(), format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    pool_id = SelectField('Бассейн', coerce=int, validators=[DataRequired()])
    fish_type_id = SelectField('Вид рыбы', coerce=int, validators=[DataRequired()])
    control_desc = TextAreaField('Описание', validators=[Optional()])
    fish_number = IntegerField('Количество', validators=[DataRequired()])
    fish_biomass = FloatField('Биомасса', validators=[DataRequired()])
    fish_survival = FloatField('Выживаемость', validators=[Optional()])
    fish_biometric = TextAreaField('Биометрические показания', validators=[Optional()])
    fish_comment = TextAreaField('Комментарий', validators=[Optional()])
    submit = SubmitField('Сохранить')

class FishInventoryGraphForm(FlaskForm):
    parameter = SelectField('Параметр', choices=[
        ('fish_biomass', 'Биомасса'),
        ('fish_number', 'Количество'),
        ('fish_survival', 'Выживаемость')
    ], validators=[DataRequired()])
    start_date = DateField('Начальная дата', default=datetime.utcnow() - timedelta(days=90), format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('Конечная дата', default=datetime.utcnow() + timedelta(days=1), format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Отобразить')
