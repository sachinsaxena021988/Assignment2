
# coding: utf-8

# In[30]:


# define number of row for pattern
n =9

# loop through the number of row
for i in range(n):
    # increment till the middle of the row count
    if i < int(n/2)+1:
        for j in range(0,i+1):
            print("*",end ='')
        else :
            print("\r")
    else :
        #show the remaining row number
        for j in range(i,n):
            print("*",end='')
        else:
            print("\r")

            

