#🛑 Module in python🛑
# single py file
#create a module mymodule.py file
# use my module file

'''
import mymodule
mymodule.say_hello("Piyush")
mymodule.say_bye("Rahul")



#👉 agar Hume kisi file me kisi ek function se kaam hai to direct use hi call kar lete hai pahle module se uss fuctka name import kar lete hai 👇

from mymodule import person1
print(person1["name"])
print(person1["age"])


#👉 agar kayi sare function use karna hai to  * ka use karte hai like as ..👇

from mymodule import *
say_hello("piyush")
say_bye("karan")


#🛑 package : collection modules/py files + __init__.py

#🛑 library : collection of package and modules

# In-built library 👇

import math

a = 16
print(math.sqrt(a))

# import specific function from librery 👇

from math import factorial 

b = 5
print(factorial(b))



#👉 agar module ka name bada hai to👇
# 👉 example👇

import math
print(math.pi)

#👇short form👇

import math as m
print(m.pi)

'''
import math 

square = pow(5 , 2)
print(square)

cube = pow(5 , 3)
print(cube)