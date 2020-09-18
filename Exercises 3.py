"""
# EXERCISE 01
print("\n\t Of 1 to 100 \n")
for i in range(1,101,1):
    print (i)

# EXERCISE 02
print("\n\t Choose the interval")

n = int(input("\n Input the first of interval: "))

m = int(input("\n Input the last number of interval: "))

for i in range(n,m,1):
    print(i)

# EXERCISE 03
print("\t\n Inversing interval printing\n")

for i in range(10,0,-1):
    print(i)

# EXERCISE 04
print ("\t\n Interval of pairs numbers in 0>100 \n")

for i in range (0,101,2):
    print(i)

# EXERCISE 05
print("\t\n Sum of pairs numbers in interval 0>100 \n")

x=0

for i in range(100):

    if i%2==0:
        x+=1

print(x)

# EXERCISE 06
print("\t\n Prime numbers in interval 0>100 \n")

for i in range(100):
    if i>=2:
        if all(i%x!=0 for x in range(2,i)):
            print (i)
"""