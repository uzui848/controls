# Print all even numbers from 1 to 20

for i in range(1,20+1):
    if i %2 != 0:
        print(i,end = " ")

#user input

num = int(input("enter any number: "))

for i in range(1,num+1):
    if i % 2 == 0:
        print(i,end = " ")