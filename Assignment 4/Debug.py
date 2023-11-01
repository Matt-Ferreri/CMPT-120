
def printHello():
    print("Hello")
    
def printName(x):
    print(x)
    
def addition(x, y):
    sum=x+y
    #add x and y together and return them
    return sum

def smaller(i, j):
    if(i<j):
        return i
    if(j<i):
        return j
    if(i==j):
        return 0
    #if i is smaller than j, return i
    #if j is smaller than i, return j
    #if they're even, return 0

def main():
    #call the printHello function here
    printHello()
    #call printName and give it the parameter of your name
    printName("Matt")

    y= 10
    x= 20
    #What do we put in here to make it work?
    print(addition(x,y))
    
    i = int(input("Enter number 1"))
    j = int(input("Enter number 2"))
    #what go here?
    print(smaller(i,j))




main()
