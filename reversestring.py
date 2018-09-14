
# coding: utf-8

# In[13]:


# define user input from console
user_input =input("please provide string to reverse :")

#define variable to hold reverse string value
reverse =""

#reverse user input
for i in user_input: 
    reverse = i + reverse

print(reverse)

