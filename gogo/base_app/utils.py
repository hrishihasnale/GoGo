import datetime,time
import pandas as pd
import calendar, logging
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


"""
To get passed key value from request object
"""
def get_request_value(request, key, default_value):
    if key in request.data:
        return request.data[key]

    return default_value



def get_date_millis_from_string(str_value, str_format):
    return datetime.datetime.strptime(str_value, str_format).timestamp()

def get_date_from_string(str_value, str_format):
    return datetime.datetime.strptime(str_value, str_format)

def get_date_float_to_string(float_value,str_format):
    return time.strftime(str_format,time.gmtime(float_value))

def get_end_date_from_date(str_value, str_format):
    date_val = datetime.datetime.strptime(str_value, str_format)
    day = calendar.monthrange(date_val.year, date_val.month)[1]

    return datetime.datetime.strptime('{year}-{month}-{date}'.format(year=date_val.year, month=date_val.month, date=day), "%Y-%m-%d").timestamp()


"""
To get user accessibility for passed module 
"""
def is_user_has_permission(request, module_name):
    return True
