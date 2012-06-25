#archibold_acheampong

userInput = int(raw_input("Enter a number = "))

#initialize variables  
tempVar = 0
i = 0

#determine number of digits
number = userInput

while number >= 10:
  number = number/10
  i += 1
print 'the number of digits you entered is',i+1

#compute reversed number
number = userInput

while number >= 10:
  tempVar = tempVar + (number%10)*10**i
  print (number%10)*10**i
  number = number/10
  i -= 1

else:
  print (number%10)*10**i
  number = tempVar + number
  print 'The reversed number is', number
