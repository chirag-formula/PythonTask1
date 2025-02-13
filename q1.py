#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''question 1 '''

n = int(input("how many strings you want to enter: "))
li =[]
counter={ }
for i in range (n) :
    stri = input("enter your strings: ")
    li.append(stri)

for i in li:
    for letters in i :
        if letters in counter:
            counter[letters] = counter[letters] + 1
        else :
            counter[letters] = 1 
print(counter)    

