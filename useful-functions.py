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
               
        match = re.search(r'(^[a-zA-Z_0-9\.\+_-]+)@[a-zA-Z].[a-zA-Z\.]+$', email)
        
        if match: return True                

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
    
if __name__ == "__main__": 
    main()