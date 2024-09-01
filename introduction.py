#!/usr/bin/env python
# coding: utf-8

# # IQB Crash Course Python Scripting in BMB 
# # Introduction
# This lesson covers some Python basics like creating variables,loops and logic

# <div class="overview-this-is-a-title overview">
# <p class="overview-title">Overview</p>
# <p>Questions</p>
#     <ul>
#         <li> What is the basic syntax of the python programming language?
#     </ul>
# <p>Objectives:</p>
#     <ul>
#         <li> Assign values to variables
#         <li> Use the print function to check how the code is working.
#         <li> Use multiple assignment to assign several variables at once.
#         <li> Use a for loop to perform the same action on the items in a list
#     </ul>
# </div>

# ## Getting Started
# Python is a computer programming language that has become ubiquitous in scientific programming.  Our lessons will run python *interactively* through a python interpreter inside a Jupyter notebook.  The [setup](setup.ipynb) page should have provided information on how to install and start a Jupyter notebook.  Everything included in a code block is something you could type into your python interpreter and evaluate.
# 
# ### Setting up your Jupyter notebooks
# If you are reading this page, then you have succeeded in gaining access to Jupyter notebooks. Now, we will use the notebook to execute Python code. Jupyter notebooks are divided into cells. You run a Jupyter notebook one cell at a time. To execute a cell, click inside the cell and press `shift+enter`.
# 
# In the upper left corner, click where it says "Untitled" and change the name to "IQB Crash Course". We have now changed the name of the Jupyter Notebook.
# 
# Jupyter notebooks allow us to also use something called **markdown** in selected cells. We can use markdown to write descriptions about our notebooks for others to read. It's a good practice to have your first cell be markdown to explain the purpose of the notebook. Let's do that in our first cell. Click inside the first cell, then on the top of the screen select Markdown from the dropdown menu that says *Code*. 
# 
# Now, return to the cell and type the following:
# 
# ```{eval-rst}
# 
#     # IQB Crash Course Python Scripting in BMB
#     ## Introduction
# 
#     This lesson covers Python basics like variable creation 
#     and assignment and using the Jupyter notebook
# ```
# 
# 

# ## Assigning variables and data types
# 
# Any python interpreter can work just like a calculator.  This is not very useful. Type the following into the next cell of your Jupyter notebook.

# In[1]:


3+7


# variable_name = variable_value

# In[2]:


# Calculating Michealis-Menten Kinetics
Km = 15.0         # Km = 15 micromolar
Vmax= 100.0       #Vmax = 100.0 nanomoles/sec
S_conc = 8.0
velocity = Vmax * S_conc /(Km + S_conc)


# In[3]:


print(velocity)


# In[4]:


print(velocity)


# In[5]:


velocity*1000
print(velocity)
#immutable: bir kez oluşturulduktan sonra değiştirilemez


# In[6]:


velocity= velocity*1000
print(velocity)


# In[7]:


#change the value of velocity to the original value 
velocity = velocity/1000
v_per_min = velocity *60
print(velocity)
print(v_per_min)


# ### Assigning multiple variables at one time

# In[8]:


#i can assign all these variables at once
Km,Vmax,S_conc = 15.0, 100.0, 10.0
velocity = Vmax * S_conc /(Km + S_conc)
print(velocity)


# ## Data types

# In[9]:


type(velocity)


# In[10]:


type(12)


# In[11]:


velocity_string= str(velocity)
type(velocity_string)


# ## Lists
# 
# Python assigns special meanings to square brackets \[\], parentheses () and curly brackets {}, so you must be very careful with these characters.

# In[12]:


S_conc = [12.0, 13.0,1.0,14.0]
type(S_conc)


# In[13]:


#list: köşeli parantez
#set : normal parantez
#tupple:süslü parantez


# In[14]:


S_leng = len(S_conc)
print("This list contains" , S_leng, "substrate concentraitons.")


# In[15]:


print(S_conc[0])
#pythonda ilk eleman 0 ile gösteriliyor


# In[16]:


S_conc_nm = S_conc[3] * 1000
print(S_conc_nm)


# You can address individual elements of a list at any time

# ## Slices

# new_list = list_name(start:end)

# In[17]:


short_list = S_conc[0:3]
print(short_list)


# In[18]:


#**Check your understanding** 

#What does the following code print? 


slice1 = S_conc[3:]
slice2 = S_conc[:2]
print(S_conc)
print('slice1 is', slice1)
print('slice2 is', slice2)


# ## Repeating an operation many times: for loops
# Often, you will want to do something to every element of a list.  The structure
# to do this is called a `for` loop.  The general structure of a `for` loop is
# ```python
# for variable in list:
#     do things using variable
# ```

# In[19]:


for number in S_conc:
    velocity = Vmax* number/(Km +number)
    print(velocity)
    


# In[20]:


total = 0 #total değişkeni, toplamı saklamak için kullanılır
for i in range(1, 11):
    total += i #total = total + i anlamına gelir
    #her döngüde i değerini total değişkenine ekler
print("Toplam:", total)


# In[21]:


word = "Python"
for char in word:
    print(char)


# In[22]:


for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# In[23]:


n = 4
factorial = 1 #faktöriyel hesaplamasının sonucunu saklamak için kullanılır
for i in range(1, n + 1):
    factorial = factorial* i
print(f"{n}! =", factorial)


# range(start, stop) şeklinde kullanıldığında, start değeri dahil edilirken, stop değeri dahil edilmez.

# In[24]:


for i in range(6):
    print(i)


# In[25]:


#f-STRİNG NEDİR ? 
name = "Büşra"
age = 25
result = f"My name is {name} and I am {age} years old."
print(result)


# In[27]:


S_conc 


# In[30]:


for number in S_conc:
    velocity = Vmax*number/(Km + number)
    velocities.append(velocity)
    
print(velocities)    


# In[29]:


velocities = []


# In[32]:


velocities.append(13.0)


# In[33]:


print(velocities)


# ## Making choices: Logic Statements
# 

# Other logic operations include
# - equal to `==`
# - not equal to `!=`
# - greater than `>`
# - less than `<`
# - greater than or equal to `>=`
# - less than or equal to `<=`
# 
# You can also use `and`, `or`, and `not` to check more than one condition.

# In[35]:


Km, Vmax = 25.0, 200.0
substrate_concs = [10.0, 20.0,40.0,80.0,100.0]
linear_mm = []


# In[36]:


for number in substrate_concs:
    if number < Km:
        V_linear = Vmax* number /(Km +number)
        linear_mm.append(V_linear)
        
print(linear_mm)        


# In[37]:


muhafaza = []
border, rule = 18, 10
ages_of_children = [12.0,14.0,15.0,11.0,14.0]

for number in ages_of_children:
    if number < border:
        new_formula = border*number /(2*rule)
        muhafaza.append(new_formula)
        
print(muhafaza)        
        


# In[42]:


number_list= []
String_list = []
conc_list = ['1.0', 2.0, 5.0, '14.0', 20.0]

for i in conc_list:
    if i == str:
        String_list.append(i)
print(String_list)   

    if i == float :
        number_list.append(i)
print(number_list)

        
    


# In[43]:


number_list = []
String_list = []
conc_list = ['1.0', 2.0, 5.0, '14.0', 20.0]

for i in conc_list:
    if isinstance(i, str):
        String_list.append(i)
    elif isinstance(i, float):
        number_list.append(i)

print("String_list:", String_list)
print("number_list:", number_list)


# In[ ]:


##isinstance kullanım örnekleri
my_list = [1, 2, 3]

if isinstance(my_list, list):
    print(f"{my_list} bir liste.")
else:
    print(f"{my_list} bir liste değil.")


# **Exercise**
# 
# The following list contains some floating point numbers and some numbers which have been saved as strings.  Copy this list exactly into your code. </p>
# 
# ```python
# conc_list = ['1.0', 2.0, 5.0, '14.0', 20.0]
# ```
# Set up a `for` loop to go over each element of `S_list`.  If the element is a string (str), recast it as a float.  Save **all** of the numbers to a new list called number_list.  Pay close attention to your indentation!

# ## A note about jupyter notebooks
# If you use the jupyter notebook for your python interpreter, the notebook only executes the current code block.  This can have several unintended consequences. If you change a value and then go back and run an earlier code block, it will use the new value, not the first defined value, which may give you incorrect analysis.  Similarly, if you open your jupyter notebook later, and try to run a code block in the middle, it may tell you that your variables are undefined, even though you can clearly see them defined in earlier code blocks.  But if you didn't re-run those code blocks, then python doesn't know they exist.  

# In[ ]:




