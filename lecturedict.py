# for anagrams

word_1 = "silent"
word_2 = "listen"

freq = {}

for ch in word_1:
    if ch in freq:
        freq[ch] += 1
    else:
       freq[ch] =1
       
       
for ch in word_2:
    if ch in freq:
        freq[ch] -= 1
    else:
         print("false")
         break
       
for values in freq.values():
    if values!= 0:
        print("false")
        break
else:
        print("true")
        