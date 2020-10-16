#global numberInput
numberInput=int(input("Number\n"))
def isPrime(numberInput):
    for count in range(2,int(numberInput/2)):
        if int(numberInput)%count==0:
            return False
    return True
count2=3
while count2 <=numberInput:
    if isPrime(count2)==True and isPrime(count2+2)==True:
        print(count2,count2+2)
    count2+=2
