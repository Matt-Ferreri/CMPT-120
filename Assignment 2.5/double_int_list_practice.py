def main():
  
  #set this to any double
  doubleValue = 32.5
  
  #set this to any int
  intValue = 14
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue+intValue)
  print(doubleValue-intValue)
  print(doubleValue*intValue)
  print(doubleValue/intValue)
  
  #populate this list
  myFriends = ["Tanner","Piper","Alex","Joe","Sean","Tommy"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [7,12,43,65,101]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[1]+fiveNumbers[2])
  print(fiveNumbers[4]-fiveNumbers[0])
  print(fiveNumbers[1]*fiveNumbers[2])
  print(fiveNumbers[3]/fiveNumbers[1])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[2]=37
  fiveNumbers[4]=452
  #print out the list
  print(fiveNumbers)
  
main()
