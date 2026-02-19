# for duplicate in dictionary

num = [1,2,3,2,4,1,5,5]

freq ={}

for i in num:
    if i in freq:
        freq[i] += 1
        
    else:
        freq[i] = 1

for i in freq:
       if freq[i] > 1:
        print(i)
     
    
        
      