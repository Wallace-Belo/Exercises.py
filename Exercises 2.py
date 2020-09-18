"""
# EXERCISE 01
print ("\n \t ===Positive or Negative=== \n")
#--
n = int(input("Input a number: "))
#--
if n >= 0:
    print("Positive!")
else:
    print("Negative!")

# EXERCISE 02 
print("\n \t ===Pair or Odd=== \n")

n = int(input("Input a number: "))

if n %2==0:
    print ("\n Pair!")
else:
    print("\n Odd!")

# EXERCISE 03
print ("\n \t Who is highest? \n")

n1 = int(input("Input the first number: "))
n2 = int(input("\n Input the second number: "))

if n1>n2:
    print("\n The first number is higher then second! \n")
else:
    print("\n The second number is higher then first! \n")

# EXERCISE 04
print ("\n \t Higher or lesser of age")

n = int(input("\n Input your: "))

if n>18:
    print("Higher of age!")
else:
    print("Lesser of age!")

# EXERCISE 05
print("\n \t How old was your mother when you're born ")

n1=int(input("\n Input your age: "))
n2=int(input("\n Input your mother age: "))
n3= n2-n1

print("\n Your mother was %i years old, when you born!", %n3)

# EXERCISE 06
print ("\n\t Printing 50x the same char \n")
char_str="-"
print("Printing: \n %s \n" %(char_str*50))

# EXERCISE 07
print("\n \t ===Pair or Odd=== \n")

n = int(input("Input a number: "))

if n %2==0:
    print ("\n Pair!")
else:
    print("\n Odd!")

# EXERCISE 08
print("\n\t Higher e Lesser")

n1=int(input("\n Input the first number: "))
n2=int(input("\n Input the second number: "))

if n1>n2:
    print("\n The higher number is %i, the first number typed. \nAnd the lesser is %i, the second number typed. " %(n1, n2))
else:
    print("\n The higher number is %i, the second number typed. \nAnd the lesser is %i, the first number typed. " %(n2, n1))
"""