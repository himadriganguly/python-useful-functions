import re

class usefulFunc():
    
    def isprime(self, num): 
          
        if num == 0:
            print("Number 0 is not a prime number.")
            return False
        elif num == 1:
            print("Number 1 is special case.")
            return False   
             
        for i in range(2,num):
            if num % i == 0:
                #print("The number {} is not prime".format(num))
                return False
                    
        print("The number {} is prime".format(num))
    
    
    def inclusive_range(self, *args):
                
        numargs = len(args)
        
        step = 1
        
        if numargs < 1:
            raise TypeError('Atleats one arguement is required')
        elif numargs == 1:
            start = 0
            stop = args[0]
        elif numargs == 2:
            (start,stop) = args 
        elif numargs == 3:
            (start,stop,step) = args
        else:
            raise TypeError('Number of arguement exceeds')
        
        i = start
        while i <= stop:
            yield(i)
            i += step
    
    
    def email_validate(self, email): 
               
        match = re.search(r'(^[a-zA-Z0-9\.\+_-]+)@[a-zA-Z].[a-zA-Z\.]+$', email)
        
        if match: return True    
    
    def binary_addition(self, first_num, second_num):
        
        bnum1 = str(bin(first_num)[2:])
        bnum2 = str(bin(second_num)[2:])
                
        maxlen = max( len(str(bnum1)), len(str(bnum2)) )
        
        bnum1 = bnum1.zfill(maxlen)
        bnum2 = bnum2.zfill(maxlen)
        
        #http://stackoverflow.com/questions/21420447/need-help-in-adding-binary-numbers-in-python
        
        result = ''
        carry = 0
        
        for i in range(maxlen-1, -1, -1):
            r = carry
            r += 1 if bnum1[i] == '1' else 0
            r += 1 if bnum2[i] == '1' else 0
            
            result = ('1' if r%2 == 1 else '0') + result
            carry = 0 if r < 2 else 1 
        
        if carry != 0: result = '1' + result 
                        
        return(result)

def main():
    
    func = usefulFunc()
    
    for i in range(100):
        func.isprime(i)
        
    print("\n")
        
    for i in func.inclusive_range(5,25,2):
        print(i)    
    
    print("\n")
    
    if func.email_validate("test-user@localhost.co.in"):
        print("It is a valid email.")
    else:
        print("Not a valid email.") 
    
    print(func.binary_addition(2, 13))  
    
if __name__ == "__main__": 
    main()