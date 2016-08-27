#! python3
# passwordDetection -Write a function that uses regular expressions to make sure the password string it is passed is strong. 
import re
def checkLen(pwd):
    return len(pwd) >= 8
    
def checkUpper(pwd):
    upperReg = re.compile(r'[A-Z]+')
    match = upperReg.search(pwd)
    if match:
        return True
    else:
        return False
        
def checkLower(pwd):
    lowerReg = re.compile(r'[a-z]+')
    match = lowerReg.search(pwd)
    if match:
        return True
    else:
        return False

def checkNum(pwd):
    numReg = re.compile(r'[0-9]+')
    match = numReg.search(pwd)
    if match:
        return True
    else:
        return False

def checkPassword(pwd):
    return(checkLen(pwd) and checkLower(pwd) and checkNum(pwd) and checkUpper(pwd))
    
def main():
    password = input("请输入密码： ")
    if checkPassword(password):
        print("密码够强")
    else:
        print("密码太弱")
            
if __name__ == '__main__':
    while True:
        main()