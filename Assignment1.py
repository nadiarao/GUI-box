from abc import ABC, abstractmethod
import random
import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Shape:
    def __init__(self):
        self.__color = "red"

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    @abstractmethod
    def find_area(self):
        pass
    
    @abstractmethod
    def find_volume(self):
        pass

    def display(self):
        print(type(self).__name__)

def display_shapes(shapes_list):
 for shape in shapes_list:
        shape.display()
        print("Area:", shape.find_area())
        if isinstance(shape, Cube):
            print("Volume:", shape.find_volume())
        print()

#saving the file
def save_to_file(filename, shapes_list):
   # try:
     with open(filename, 'w') as f:
        for shape in shapes_list:
            f.write(shape.display() + '\n')
            f.write("Area: " + str(shape.find_area()) + '\n')
            if isinstance(shape, Cube):
                f.write("Volume: " + str(shape.find_volume()) + '\n')
            f.write('\n')
    # print("File saved successfully.", filename) 
   # except Exception as e:
    #    print("An error occurred while saving the file:",e) 

# messagebox 
def display_with_messagebox(shapes_list):
    result = ""
    for shape in shapes_list:
        result += shape.display() + '\n'
        result += "Area: " + str(shape.find_area()) + '\n'
        if isinstance(shape, Cube):
            result += "Volume: " + str(shape.find_volume()) + '\n'
        result += '\n'
    messagebox.showinfo("Shapes Information", result)

shapes_list = []
shape_counts = {'Circle': 0, 'Square': 0, 'Cube': 0}

#Circle
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.__radius = 1

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def find_area(self):
        return math.pi * self.__radius ** 2
    
    def display(self):
        return "Circle type"

#Square
class Square(Shape):
    def __init__(self):
        super().__init__()
        self.__side = 2.3

    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def find_area(self):
        return self.__side ** 2

    def display(self):
        return "Square type"

#Cube
class Cube(Shape):
    def __init__(self):
        super().__init__()
        self.__length = 3
        self.__width = 3
        self.__height = 3

    def set_dimensions(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def get_dimensions(self):
        return self.__length, self.__width, self.__height

    def find_volume(self):
        return self.__length * self.__width * self.__height     
    
    def display(self):
        return "Cube type"


shapes_list = []
shape_counts = {'Circle': 0, 'Square': 0, 'Cube': 0}

#Loop
for _ in range(15):
    choice = random.randint(1, 3)

    if choice == 1:
        shape = Circle()
        shape_counts['Circle'] += 1
    elif choice == 2:
        shape = Square()
        shape_counts['Square'] += 1
    else:
        shape = Cube()
        shape_counts['Cube'] += 1

    shapes_list.append(shape)

for shape in shapes_list:
    shape.display()
    print("Area:", shape.find_area())
    if isinstance(shape, Cube):
        print("Volume:", shape.find_volume())
    print()

#How do you want to display the output of the data
display_option = input("Select display option (a/b/c): ")

if display_option == 'a':
    display_shapes(shapes_list)

# Pie chart visualization
    labels = list(shape_counts.keys())
    sizes = list(shape_counts.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Shape Distribution")
    plt.show()   

#Saving in a file
elif display_option == 'b':
    file_name = input("Enter file name to save results: ")
    save_to_file(file_name, shapes_list)
    print("Results saved to", file_name)

#messagebox    
elif display_option == 'c':
    display_with_messagebox(shapes_list)
else:
    print("Invalid option")    

                

