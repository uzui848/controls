#Take n and print all multiples of 3 from 1 to n.

num = int(input("enter any number: "))

for i in range(1,num+1):
    if i % 3 == 0:
        print(i,end = " ")