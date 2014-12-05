'''
Created on 2014.12.4

@author: apple
'''
import re
import pandas.io.data as web
import datetime
from Exceptions import *

def IsValidStockName(stock_name):
    """
    Check whether the input is a valid stock name.
    """
    if isinstance(stock_name, str):
        #Check whether input of list has a valid form
        try:
            df =web.DataReader(stock_name,'yahoo')
        except:
            return False
        else:
            return True
    else:
        return False
def ParseStockName(stock_name):
    """
    Parse stock name when the input is a valid stock name.
    """
    if IsValidStockName(stock_name):
        return stock_name

def IsValidDate(date_string):
    """
    Check whether the input is a valid date.
    """
    if isinstance(date_string, str):
        #Check whether input of list has a valid form
        try:
            datetime.datetime.strptime(date_string, '%Y/%m/%d')
            return True
        except ValueError:
            return False
    else:
        return False

def ParseDate(date_string):
    """
    Parse when the input is a valid date.
    """
    if IsValidDate(date_string):
        return datetime.datetime.strptime(date_string, '%Y/%m/%d')
        

def IsEmptyInput(stock_name,start_date,end_date):
    """
    Check whether the input is null or not.
    """
    if stock_name == '' or start_date == '' or end_date == '':
        return True
    else:
        return False
    
        