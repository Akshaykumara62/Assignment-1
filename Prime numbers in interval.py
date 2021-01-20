#!/usr/bin/env python
# coding: utf-8

# In[4]:


lower = int(input('enter lower bound:'))
upper = int(input('enter upper bound:'))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# In[ ]:





# In[ ]:




