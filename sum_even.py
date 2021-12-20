#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

var_int = 1234
sum_even = 0
a = abs(((var_int//1000)%2)-1)
b = abs(((var_int%1000//100)%2)-1)
c = abs(((var_int%100//10)%2)-1)
d = abs(((var_int%10)%2)-1)
a1 = var_int//1000
b1 = var_int%1000//100
c1 = var_int%100//10
d1 = var_int%10
sum_even = (a*a1)+(b*b1)+(c*c1)+(d*d1)
print(sum_even)