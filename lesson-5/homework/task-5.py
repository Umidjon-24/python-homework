#TASK 5
def is_prime(n):
    count = 0
    if n>0:
        for i in range (2,int(n**0.5)):
            if n%i == 0:
                count+=1
        if count == 0:
            return True
        else: return False
    else:
        return "Only positive number!!!"
  
        
print(is_prime(105))