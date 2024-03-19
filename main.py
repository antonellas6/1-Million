# Antonella Sanchez
# 11/9/2023
# print all even numbers between 1 and 1 million
counter = 1
# create a while loop counter is beween 1 and 1 million
counter = 1
while counter <= 1000000:
# inside the loop diviible counter by 2
# in another variable
 evenNumber = counter % 2
# the remainder should be 0 when number is even
# condition to print only even numbers
if evenNumber == 0:
 print(counter)