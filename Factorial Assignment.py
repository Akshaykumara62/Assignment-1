#!/usr/bin/env python
# coding: utf-8

# In[1]:


#5! = 1*2*3*4*5 =120


# In[13]:


factorial = 1
num = 5

if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial * i
    print("the factorial of",num,"is",factorial)
    


# In[ ]:





# In[ ]:





# In[ ]:




