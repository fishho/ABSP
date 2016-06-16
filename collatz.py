#recursion version
def collatz(n):
    if(n%2==0):
        n=n//2
    else:
       n=3*n+1
    print(n)
    if(n!=1):
       return collatz(n)
    else:
        return 1;

def collatz1(n):
    if(n%2==0):
       n=n//2
    else:
       n=3*n+1
    print(n)
    return n;   

def validate(inputContent):
    if(not inputContent.isdigit()):
        print(inputContent +'is not a inter number\n')
        inputContent = input("please enter a integer number:\n")
        return validate(inputContent)
    else:
        return int(inputContent)
    
inputContent = input('please enter a integer number:\n')    
mynumber = validate(inputContent)
if(input('please enter 0 or 1 for collatz an collatz1:\n') == '1'):
    print("\n")
    while(mynumber != 1):
        mynumber =collatz1(mynumber);
        
#default is recursion collatz
else:
    print("\n")
    collatz(mynumber)
