#Take n and print the sum of numbers from 1 to n.

n = int(input("enter any number: "))

count = 0
for i in range(1,n+1):
  
    count +=i*i

print(count)