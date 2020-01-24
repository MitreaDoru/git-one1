def collatz(number):
 try:  
    while number != 1:  
      if number % 2 == 0:
           number = number // 2
           print(number)
      elif number % 2 == 1:
           number = 3 * number + 1
           print(number)
 except ValueError:
     print("Must enter an integer")
r = int(input("Enter a number:"))
collatz(r)