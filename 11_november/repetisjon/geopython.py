import math
import matplotlib.pyplot as plt

def solve_function(f,x):
	return eval(f)

f = input("give us a fuction f(x): ")

function_range = {"lowerbound" : int(input("lowerbound: ")), "upperbound" : int(input("upperbound: "))}

yval = [round(0.05 * x,2) for x in range(function_range["lowerbound"]*20,function_range["upperbound"]*20+1)]

ys = []
xs = []

for y in yval:
	xs.append(solve_function(f,y))
	ys.append(y)
plt.plot(ys,xs,"o")

x = int(input("pick an x value to solve for: "))
fx = solve_function(f,x)
plt.plot(x,fx,"x")

plt.show()