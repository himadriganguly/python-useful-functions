#!/usr/bin/env python


import re

    
def isprime(n):    
    '''
    >>> for n in inclusive_range(0, 10):
    ...    print('{0} is prime: {1}'.format(n, isprime(n)))
    ...
    0 is prime: False
    1 is prime: False
    2 is prime: True
    3 is prime: True
    4 is prime: False
    5 is prime: True
    6 is prime: False
    7 is prime: True
    8 is prime: False
    9 is prime: False
    10 is prime: False
    '''   
    if n == 0:
        return False
    elif n == 1:
        return False   
         
    for i in range(2, n):
        if n % i == 0:
            return False
                
    return True


def inclusive_range(start=0, stop=0, step=1):
    '''
    >>> list(inclusive_range(-10, 10, 2))
    [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    '''
    _range = list(range(start, stop, step))
    _range.append(stop)

    return iter(_range) 


def valid_email(email):      
    '''
    >>> valid_email('test-user@localhost.co.in')
    True
    >>> valid_email('te$t-user@localhost.co.in')
    False
    '''     
    match = re.search(r'(^[a-zA-Z0-9\.\+_-]+)@[a-zA-Z].[a-zA-Z\.]+$', email)
    
    if match: 
        return True

    return False 


def binary_addition(*args):
    '''
    >>> binary_addition(2, 13)
    '1111'
    >>> binary_addition(2, 13, 4, 77)
    '1100000'
    '''    
    return bin(sum(args))[2:]  
    

if __name__ == "__main__": 
    import doctest
    doctest.testmod()
    
