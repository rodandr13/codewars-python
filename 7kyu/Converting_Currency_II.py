"""
Given the current exchange rate between the USD and the EUR is 1.1363636 write a function that will accept the Curency type to be returned and a list of the amounts that need to be converted.

Don't forget this is a currency so the result will need to be rounded to the second decimal.

'USD' Return format should be '$100,000.00'

'EUR' Return format for this kata should be '100,000.00€'

to_currency is a string with values 'USD','EUR' , values_list is a list of floats

solution(to_currency,values)
"""


def solution(to_cur,value):
    currency = {
        'USD': '€',
        'EUR': '$'
    }
    rate = 1.1363636
    if to_cur == 'EUR':
        return list(map(lambda x: '{:,.2f}'.format(round(x / rate, 2)) + '€', value))
    temp = list(map(lambda x: '$' + '{:,.2f}'.format(round(x * rate, 2)), value))
    return temp
