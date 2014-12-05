'''
Created on 2014.12.4

@author: apple
'''

class StockNameInputException(Exception):
    """
    Raise when the input is not a stock name in the yahoo financial data.
    """
    def __str__(self):
        return "The input is invalid. It must be a stock name in the yahoo financial data."
    
class DateInputException(Exception):
    """
    Raise when the input is not date form.
    """
    def __str__(self):
        return "The input is invalid. It must contain year, month, and day, separated by '/', such as 2011/1/1."
    
class EmptyInputException(Exception):
    """
    Raise when the input of stock name or the input of date is null.
    """
    def __str__(self):
        return "The input of stock name or date is null, please enter the input."
    
class ConnectInternetException(Exception):
    """
    Raise when the Internet can not be connected.
    """
    def __str__(self):
        return "The Internet is not available, please check your connection."
    