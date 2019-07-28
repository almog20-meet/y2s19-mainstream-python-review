# Part 2 of the Python Review la

def prime (n):
        if (n>1):
                for i in range(2,y):
                        if (y % i) ==0:
                                return False
        else:
                return True
def encode(x, y):
        while not prime(x):
                x+=1
        while not prime(y):
                y+=1
        if (1 < y) and (y< 250) and (500 < x) and (x < 1000):
                return (x*y)
        else:
                print ("Invalid input: Outside range.")
                return None

def decode(coded_message):
        for y in range(2,250)
                print (y)
                if not prime(y):
                        continue
                x= coded_message / y
                if (prime(x) and 500 < x and x<1000 ) :
                        return (x , y)
        
