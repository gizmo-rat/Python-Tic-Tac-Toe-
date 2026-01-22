import numpy as np
"""name = input("Enter your name: ")
print("Welcome to Python:" , name)

list1 = ["X","Y","Z"]
list2 = [1,5,7,9,3]
list3 = [True,False,False]

print(len(list1))
print(len(list2))
print(len(list3))

numbers = (10,20,30,40,50)

print("Tuple:",numbers)
#Numbers[0] = 5 #creates an error
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("Length:", len(numbers))

print("Elements in the tuple:")
for num in numbers:
    print(num)
    
import numpy as np

arr = np.array((1,2,3,4,5))

print(arr)
    
numbers = np.array([10,20,30,40,50])

print("Array:",numbers)

print("Sum:",np.sum(numbers))
print("Mean:",np.mean(numbers))
print("Maximum:",np.max(numbers))
print("Minimum:",np.min(numbers))

double_numbers = numbers * 2
print("Array after multiplying by 2:",double_numbers)

def sum_and_average(arr):
    total = np.sum(arr)
    average = np.mean(arr)
    return total, average

numbers = np.array([10,20,30,40,50])
s,avg = sum_and_average(numbers)
print("Sum:",s)
print("Average:",avg)

import numpy as np
grid = np.zeros((5,5))
grid[2,:] = 1
grid[:,2] = 1
print(grid)

import random
def guess_game():
    number = random.randint(1,10)
    guess = int(input("Guess a number (1-10) : "))
    if guess == number:
        print("Correct!")
    else:
        print("Wrong! The number was : ",number)

guess_game()"""

import matplotlib.pyplot as plt

#x2 = np.array([1,3])
#y2 = np.array([3,1])
#xpoints = np.array([2,6,2,6,2,6])
#ypoints = np.array([1,2,3,4,5,6])
#xpoints = np.array([1,2,6,8])
#ypoints = np.array([3,8,1,10])
#newxpoints = np.append(xpoints,[9,17])
#print(newxpoints)

def show():
    xpoints = np.array([1,1])
    ypoints = np.array([0,3])
    crosspoints = [.1,.9]
    crosspoints2 = [.9,.1]
    plt.figure(figsize=(5,5))
    plt.plot(xpoints, ypoints, color = 'black')
    plt.plot(xpoints*2,ypoints, color = 'black')
    plt.plot(ypoints,xpoints, color = 'black')
    plt.plot(ypoints,xpoints*2, color = 'black')
    plt.plot(crosspoints,crosspoints, color = 'b')
    plt.plot(crosspoints,crosspoints2, color = 'b')
    plt.show()


show()

