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


def binary_addition(n_1, n_2):
    '''
    >>> binary_addition(2, 13)
    '1111'
    '''    
    bn_1 = bin(n_1)[2:]
    bn_2 = bin(n_2)[2:]
            
    maxlen = max(len(bn_1), len(bn_2))
    
    bn_1 = bn_1.zfill(maxlen)
    bn_2 = bn_2.zfill(maxlen)
    
    #http://stackoverflow.com/questions/21420447/need-help-in-adding-binary-numbers-in-python
    
    result = ''
    carry = 0
    
    for i in range(maxlen-1, -1, -1):
        r = carry
        r += 1 if bn_1[i] == '1' else 0
        r += 1 if bn_2[i] == '1' else 0
        
        result = ('1' if r%2 == 1 else '0') + result
        carry = 0 if r < 2 else 1 
    
    if carry != 0: result = '1' + result 
                    
    return result  
    

if __name__ == "__main__": 
    import doctest
    doctest.testmod()
    
