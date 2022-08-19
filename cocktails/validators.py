import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError


def validate_measurements(value):
    '''
    Checks the ingredient measures are valid units
    '''
    ureg = pint.UnitRegistry()
    try:
        unit_instance = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f'{value} is not a valid unit of measure')
    except:
        raise ValidationError(f'{value} is not a valid unit of measure')
