#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".

var_int = 2111
sum_even = 0
a = var_int//1000%2
b = var_int%1000//100%2
c = var_int%100//10%2
d = var_int%10%2
a1 = var_int//1000
b1 = var_int%1000//100
c1 = var_int%100//10
d1 = var_int%10
sum_even = (a*a1)+(b*b1)+(c*c1)+(d*d1)
print(sum_even)