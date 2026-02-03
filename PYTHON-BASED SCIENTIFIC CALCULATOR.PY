import tkinter as tk
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from tkinter import simpledialog
from math import perm
from math import comb
from tkinter import messagebox
from sympy import symbols
from matplotlib.figure import Figure
from matplotlib.pyplot import hist
from matplotlib.pyplot import plot, scatter, bar, pie
from sympy import symbols, integrate, sympify



root = tk.Tk()   #creates the window,   root is a variable,     .Tk is a class,  a class is basically used to make something 
entry = tk.Entry(root, width=25, font=("arial", 24), justify="right",bg="light blue") #textbox for userinput  .Entry is a class. a class is basically used to make something 

#justify="right" makes all text inside the Entry widget appear aligned to the right.


entry.pack(side="top",pady=10, fill='x', padx=20, ipady=70) #for displaying windows # side top, bottom, left right


entry.focus_set()   # 👈ABLE TO TAKE INPUT FROM KEYBOARD


root.title("Simple Scientific Calculator")
root.geometry("400x600")  # 400 pixels wide, 600 pixels tall
root.configure(bg="lightgrey")  # Set the background color of the window


def click(value):
    entry.insert(tk.END, value)     #entry.insert (x,y) x is the starting position of index, y is the string/text to insert

def clear():
    entry.delete(0, tk.END)

                                       ################################ ------------------TRIGNOMETRIC FUNCTIONS------------------##########################################
def sin():
    input_value=float(entry.get())
    result=math.sin(float(math.radians(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)

def cos():
    input_value=float(entry.get())
    result=math.cos(float(math.radians(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)

def tan():
    input_value=float(entry.get())
    result=math.tan(float(math.radians(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)
def sec():
    input_value=float(entry.get())
    result=1/math.cos(float(math.radians(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)
def cosec():
    input_value=float(entry.get())
    result=1/math.sin(float(math.radians(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)
def cot():
    input_value=float(entry.get())
    result=1/math.tan(float(math.radians(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)


                                       ################################ ------------------HYPERBOLIC TRIGNOMETRIC FUNCTIONS------------------##########################################



def sinh():
    input_value=float(entry.get())
    result=math.sinh(float(input_value))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)

def cosh():
    input_value=float(entry.get())
    result=math.cosh(float(input_value))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)

def tanh():
    input_value=float(entry.get())
    result=math.tanh(float(input_value))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)
def sech():
    input_value=float(entry.get())
    result=1/math.cosh(float(input_value))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)
def cosech():
    input_value=float(entry.get())
    result=1/math.sinh(float(input_value))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)
def coth():
    input_value=float(entry.get())
    result=1/math.tanh(float(input_value))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)







                                       ################################ ------------------INVERSE TRIGNOMETRIC FUNCTIONS------------------##########################################




def arcsin():
    input_value=float(entry.get())
    
    if -1 <= input_value <= 1:
        result=(math.degrees(np.arcsin(input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
            entry.delete(0, tk.END)
            entry.insert(0, "Error: out of range")


def arccos():
    input_value=float(entry.get())
    
    if -1 <= input_value <= 1:
        result=(math.degrees(np.arccos(input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
            entry.delete(0, tk.END)
            entry.insert(0, "Error: out of range")

def arctan():
    input_value=float(entry.get())    
    result=(math.degrees(np.arctan(input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)


def arcsec():
    input_value=float(entry.get())    #abs is absolute value
    if abs(input_value)>=1:
        result=(math.degrees(np.acos(1/input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")

def arccosec():
    input_value=float(entry.get())
    if abs(input_value)>=1:
        result=(math.degrees(np.asin(1/input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)

    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")


def arccot():
    input_value=float(entry.get())
    result=(math.degrees(np.arctan(1/input_value)))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)




                                       ################################ ------------------INVERSE HYPERBOLIC TRIGNOMETRIC FUNCTIONS------------------##########################################

def arcsinh():
    input_value=float(entry.get())
    result=(math.degrees(np.arcsinh((input_value))))
    entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
    entry.insert(0, result)

def arccosh():
    input_value=float(entry.get())
    if input_value >= 1:                       # valid range check
        result=(math.degrees(np.arccosh((input_value))))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")

def arctanh():
    input_value=float(entry.get())    
    if -1 < input_value < 1:                    # valid range check
        result=(math.degrees(np.arctanh(input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")


def arccoth():
    input_value=float(entry.get())
    if abs(input_value) > 1:                    # valid range check
        result=(math.degrees(np.arctanh(1/input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")


def arcsech():
    input_value=float(entry.get())    #abs is absolute value
    if 0 < input_value <= 1:                    # valid range for arcsech
        result=(math.degrees(np.acosh(1/input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")

def arccosech():
    input_value=float(entry.get())
    if abs(input_value)>=1:
        result=(math.degrees(np.asinh(1/input_value)))
        entry.delete(0, tk.END)    #entrty.delete (x,y) x is the start index to delete and y is the end index to delete
        entry.insert(0, result)

    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")



def sqrt():
    input_value=float(entry.get())
    if (input_value>=0):
        result=math.sqrt(input_value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")


def factorial():
    input_value=int(entry.get())
    if (input_value>=0):
        result=math.factorial(input_value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: out of range")


def cube_root():
    input_value=float(entry.get())
    result=math.cbrt(input_value)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def calculate():
    try:
        expr = entry.get()
        result = eval(expr)  # simple arithmetic evaluation
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
      

def X_power_Y():
    # Ask user for X
    x = simpledialog.askfloat("Input", "Enter value of X")
    if x is None:  # user cancelled
        return
    # Ask user for Y
    y = simpledialog.askfloat("Input", "Enter value of Y")
    if y is None:
        return

    # Calculate X^Y
    result = x ** y

    # Show result in the entry box
    entry.delete(0, tk.END)
    entry.insert(0, result)
def permutation():
    n = simpledialog.askinteger("Input", "Enter value of n")
    if n is None:  # user cancelled
        return
    # Ask user for r
    r = simpledialog.askinteger("Input", "Enter value of r")
    if r is None:
        return
    if n < 0 or r < 0 or r > n:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid input")
        return
    result = perm(n,r)

    # Show result in the entry box
    entry.delete(0, tk.END)
    entry.insert(0, result)
def combination():
    n = simpledialog.askinteger("Input", "Enter value of n")
    if n is None:  # user cancelled
        return
    # Ask user for r
    r = simpledialog.askinteger("Input", "Enter value of r")
    if r is None:
        return
    if n < 0 or r < 0 or r > n:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid input")
        return
    result = comb(n,r)

    # Show result in the entry box
    entry.delete(0, tk.END)
    entry.insert(0, result)
def X_square():
    x = simpledialog.askfloat("Input", "Enter value of n")
    result=x*x
    entry.delete(0, tk.END)
    entry.insert(0, result)
def pi():
    entry.delete(0, tk.END)
    entry.insert(0, 3.141592653589793)

def matrices():
    MATRICES = simpledialog.askinteger("Input", "CHOOSE OPTION \n PRESS 1 FOR IDENTITY MATRIX \n PRESS 2 FOR CONSTANT MATRIX \n PRESS 3 MATRIX ADDITION \n PRESS 4 MATRIX MULTIPLICATION \n PRESS 5 MATRIX DETERMINANT \n PRESS 6 FOR INVERSE OF A MATRIX \n PRESS 7 MATRIX SUBTRACTION \n PRESS 8 MATRIX TRANSPOSE \n PRESS 9 FOR TRACE OF MATRIX (SUM OF DIAGONAL ELEMENTS)")

    if(MATRICES==1):
        IDENTITY_MATRIX=simpledialog.askinteger("input", "MENTION THE SHAPE")
        MATRIX=np.eye(IDENTITY_MATRIX)
        entry.delete(0, tk.END)
        entry.insert(0, MATRIX)

        
    elif(MATRICES==2):
        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
        NUMBER_TO_BE_PRINTED=simpledialog.askinteger("input", "MENTION THE CONSTANT NMBE TO BE PRINTED ")
        FULL_FUNCTION=np.full((ROWS,COLUMNS), NUMBER_TO_BE_PRINTED)
        entry.delete(0, tk.END)
        entry.insert(0, FULL_FUNCTION)



    elif(MATRICES==3):      
        
        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
        NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX A SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
        #ask string only takes two arguments
        
        MATRIX1_INPUT_LIST=NUMBERS.split() # split into a list of strings
        FINAL_MATRIX1=np.array(MATRIX1_INPUT_LIST, dtype=float).reshape(ROWS, COLUMNS)
    

        NUMBERS2=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX B SEPERATED BY SPACE ")
        MATRIX2_INPUT_LIST=NUMBERS2.split() # split into a list of strings
        FINAL_MATRIX2=np.array(MATRIX2_INPUT_LIST, dtype=float).reshape(ROWS, COLUMNS)

        FINAL_MATRIX=FINAL_MATRIX1+FINAL_MATRIX2
        entry.delete(0, tk.END)
        entry.insert(0, str(FINAL_MATRIX))

    
    elif(MATRICES==4):

        ROWS1=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS OF MATRIX A ")
        COLUMNS1=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS OF MATRIX A ")

        ROWS2=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS OF MATRIX B ")
        COLUMNS2=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS OF MATRIX B")
    
        if(COLUMNS1!=ROWS2):
            messagebox.showerror("Error", "NUMBER OF COLUMNS IN MATRIX A IS NOT EQUAL TO NUMBER OF ROWS IN MATRIX B. MULTIPLICATION NOT POSSIBLE.")
        else:
            NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS1*COLUMNS1} ELEMENTS OF MATIX A SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
            MATRIX1_LIST=NUMBERS.split()
            FINAL_MATRIX1=np.array(MATRIX1_LIST, dtype=float).reshape(ROWS1, COLUMNS1)

            NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS2*COLUMNS2} ELEMENTS OF MATIX B SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
            MATRIX2_LIST=NUMBERS.split()
            FINAL_MATRIX2=np.array(MATRIX2_LIST, dtype=float).reshape(ROWS2, COLUMNS2)


            FINAL_MATRIX_MULTIPLIED=np.dot(FINAL_MATRIX1, FINAL_MATRIX2)
            entry.delete(0, tk.END)
            entry.insert(0, str(FINAL_MATRIX_MULTIPLIED))

    elif(MATRICES==5):

        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
      

        if (ROWS!=COLUMNS):
            messagebox.showerror("Error", "DETERMINANTS ARE ONLY POSSIBLE IN SQUARE MATRICES")
        
        else:
            NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
            MATRIX_LIST=NUMBERS.split()
            FINAL_MATRIX=np.array(MATRIX_LIST, dtype=float).reshape(ROWS, COLUMNS)
            
            DETERMINANT=np.linalg.det(FINAL_MATRIX)
            entry.delete(0, tk.END)
            entry.insert(0, str(DETERMINANT))

            
    elif(MATRICES==6):
        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
      
        if (ROWS!=COLUMNS):
            messagebox.showerror("Error", "INVERSE ARE ONLY POSSIBLE IN SQUARE MATRICES")
        
        else:
            NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
            MATRIX_LIST=NUMBERS.split()
            FINAL_MATRIX=np.array(MATRIX_LIST, dtype=float).reshape(ROWS, COLUMNS)
            DETERMINANT=np.linalg.det(FINAL_MATRIX)
            if(np.isclose(DETERMINANT,0)):
                print("INVERSE NOT POSSIBLE BECAUSE DETERMINANT IS ZERO")
            else:
                INVERSE=np.linalg.inv(FINAL_MATRIX)
                entry.delete(0, tk.END)
                entry.insert(0, str(INVERSE))
    elif(MATRICES==7):
        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
        NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX A SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
        #ask string only takes two arguments
        
        MATRIX1_INPUT_LIST=NUMBERS.split() # split into a list of strings
        FINAL_MATRIX1=np.array(MATRIX1_INPUT_LIST, dtype=float).reshape(ROWS, COLUMNS)
    

        NUMBERS2=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX B SEPERATED BY SPACE ")
        MATRIX2_INPUT_LIST=NUMBERS2.split() # split into a list of strings
        FINAL_MATRIX2=np.array(MATRIX2_INPUT_LIST, dtype=float).reshape(ROWS, COLUMNS)

        FINAL_MATRIX=FINAL_MATRIX1-FINAL_MATRIX2
        entry.delete(0, tk.END)
        entry.insert(0, str(FINAL_MATRIX))

    
    elif(MATRICES==8):

        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
        NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX A SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
        MATRIX1_INPUT_LIST=NUMBERS.split() # split into a list of strings
        FINAL_MATRIX1=np.array(MATRIX1_INPUT_LIST, dtype=float).reshape(ROWS, COLUMNS)
        TRANSPOSE=np.transpose(FINAL_MATRIX1)
        entry.delete(0, tk.END)
        entry.insert(0, str(TRANSPOSE))

    elif(MATRICES==9):

        ROWS=simpledialog.askinteger("input", "ENTER THE NUMBER OF ROWS ")
        COLUMNS=simpledialog.askinteger("input", "ENTER THE NUMBER OF COLUMNS ")
 
        NUMBERS=simpledialog.askstring("input", f"ENTER THE {ROWS*COLUMNS} ELEMENTS OF MATIX A SEPERATED BY SPACE ") # f  An f before a string makes it a formatted string literal, letting you insert variables or expressions directly using {}.
        MATRIX1_INPUT_LIST=NUMBERS.split() # split into a list of strings
        FINAL_MATRIX1=np.array(MATRIX1_INPUT_LIST, dtype=float).reshape(ROWS, COLUMNS)
        TRACE_OF_MATRIX=np.trace(FINAL_MATRIX1)
        entry.delete(0, tk.END)
        entry.insert(0, str(TRACE_OF_MATRIX))
def statistics():
    statistic= simpledialog.askinteger("Input", "CHOOSE OPTION \n PRESS 1 FOR SUM \n PRESS 2 FOR MEAN \n PRESS 3 FOR MIN \n PRESS 4 FOR MAX \n PRESS 5 FOR STANDARD DEVIATION \n PRESS 6 FOR VARIANCE \n PRESS 7 FOR MEDIAN")

    if statistic==1:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE ")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        SUM=np.sum(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(SUM))
    elif statistic==2:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        MEAN=np.mean(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(MEAN))
    elif statistic==3:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        MIN=np.min(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(MIN))
    elif statistic==4:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        MAX=np.max(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(MAX))
    elif statistic==5:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        STD=np.std(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(STD))
    elif statistic==6:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        VARIANCE=np.var(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(VARIANCE))
    elif statistic==7:
        NUMBERS=simpledialog.askstring("input", "ENTER THE NUMBERS SEPERATED BY SPACE")
        numbers=np.array([float(x) for x in NUMBERS.split()])
        MEDIAN=np.median(numbers)
        entry.delete(0, tk.END)
        entry.insert(0, str(MEDIAN))


def differentiation():

    DIFFERENTIATION= simpledialog.askinteger("Input", "CHOOSE OPTION \n DO YOU WANT TO USE SUBSTITUTION IN DIFFERENTIATION EXPRESSION\n PRESS 1 FOR YES \n PRESS 2 FOR NO \n ")

    if(DIFFERENTIATION==1):
        X=sp.symbols("x")

        EXPRESSION=simpledialog.askstring("input", "PLEASE ENTER YOUR EXPRESSION FOR DIFFERENTIATION \n DISCLAIMER ! \n USE THE VARIABLE small x \n * for Multiplication \n ** for Power ")
        
        if EXPRESSION:
            try:
                simplified=sp.sympify(EXPRESSION) #EXPRESSION is being read from input() as a string. SymPy requires a symbolic expression, not a string.
                VALUE= simpledialog.askinteger("Input", "TYPE THE VALUE THAT YOU WANT TO SUBSTITUTE ")
                ORDER= simpledialog.askinteger("Input", "WRITE THE NUMBER OF TIMES YOU WANT TO DERIVATE ")
                RESULT=sp.diff(simplified, X, ORDER) # 1 is the number of times the function is gonna derivate the polynomial
                EVALUATE=RESULT.subs(X, VALUE) #You need to specify the variable you want to substitute, e.g., RESULT.subs(X, VALUE).
                PRINT=str(EVALUATE) #Tkinter’s Entry widget (like your entry box) can only display strings,
                entry.delete(0, tk.END)
                entry.insert(0, str(PRINT))
            except:
                messagebox.showerror("Error"," INVALID INPUT!")

    elif(DIFFERENTIATION==2):
        X=sp.symbols("x")
        EXPRESSION=simpledialog.askstring("input", "PLEASE ENTER YOUR EXPRESSION FOR DIFFERENTIATION \n DISCLAIMER ! \n USE THE VARIABLE small x \n * for Multiplication \n ** for Power  ")
        if EXPRESSION:
            try:
                ORDER= simpledialog.askinteger("Input", "WRITE THE NUMBER OF TIMES YOU WANT TO DERIVATE ")
                simplified=sp.sympify(EXPRESSION) #EXPRESSION is being read from input() as a string. SymPy requires a symbolic expression, not a string.
                RESULT=sp.diff(simplified, (X, ORDER))
                PRINT=str(RESULT) #Tkinter’s Entry widget (like your entry box) can only display strings,
                entry.delete(0, tk.END)
                entry.insert(0, str(PRINT))
            except:
                messagebox.showerror("Error"," INVALID INPUT!")
def graphs():
    
    GRAPHS=simpledialog.askstring("input", "PRESS-1 FOR SCATTER PLOT \n PRESS-2 FOR HISTOGRAM \n PRESS-3 FOR PIE CHART \n PRESS-4 FOR BAR CHART \n PRESS-5 FOR LINE GRAPH")
    if GRAPHS is not None:
        GRAPHS = int(GRAPHS) 

    if(GRAPHS==1):

        TITLE_OF_DIAGRAM=simpledialog.askstring("input","TYPE THE TITLE OF DIAGRAM")
        TITLE_OF_X_AXIS=simpledialog.askstring("input","TYPE THE TITLE OF X_AXIS")
        TITLE_OF_Y_AXIS=simpledialog.askstring("input","TYPE THE TITLE OF Y_AXIS")
        X=simpledialog.askstring("input", "INPUT X_AXIS VALUES")
        Y=simpledialog.askstring("input", "INPUT Y_AXIS VALUES")
        X_AXIS=[float(i) for i in X.split()]
        Y_AXIS=[float(i) for i in Y.split()]
        COLOUR=simpledialog.askstring("input", "MENTION THE COLOR BLUE, RED, E.T.C")
        MARKER=simpledialog.askstring("input", "MENTION THE MARKER LIKE o")
        LEGEND=simpledialog.askstring("input", "TYPE THE NAME OF LEGEND")
        plt.xlabel(TITLE_OF_X_AXIS)
        plt.ylabel(TITLE_OF_Y_AXIS)
        plt.title(TITLE_OF_DIAGRAM)
        plt.scatter(X_AXIS, Y_AXIS, color=COLOUR, marker=MARKER, label=LEGEND)
        plt.legend()
        plt.grid(True)
        plt.show()



    elif(GRAPHS==2):


        SCORES=simpledialog.askstring("input","TYPE THE SCORES")
        FINAL_SCORES=[float(i) for i in SCORES.split()]
        COLOR=simpledialog.askstring("input", "MENTION THE COLOR BLUE, RED, E.T.C")
        EDGE_COLOR=simpledialog.askstring("input", "MENTION THE EDGE_COLOR BLUE, RED, E.T.C")
        BINS=simpledialog.askinteger("input","TYPE THE NUMBER OF BINS")
        X_LABEL=simpledialog.askstring("input","TYPE THE NAME OF X_AXIS ")
        Y_LABEL=simpledialog.askstring("input","TYPE THE NAME OF Y_AXIS ")
        TITLE_OF_HISTOGRAM=simpledialog.askstring("input", "TYPE THE NAME OF HISTOGRAM")
        plt.hist(FINAL_SCORES, bins=BINS, color=COLOR, edgecolor=EDGE_COLOR)
        plt.xlabel(X_LABEL)
        plt.ylabel(Y_LABEL)
        plt.title(TITLE_OF_HISTOGRAM)
        plt.show()

    elif(GRAPHS==3):

        TITLE=simpledialog.askstring("input", "TYPE THE TITLE OF PIE CHART")
        REGIONS=simpledialog.askstring("input", "TYPE THE NAME OF REGIONS IN PIE CHART SEPERATED BY SPACE")
        FINAL_REGIONS=[str(i) for i in REGIONS.split()]
        NUMBER_OF_EACH_REGION=simpledialog.askstring("input", "TYPE THE  NUMBER OF EACH REGION IN PIE CHART SEPERATED BY SPACE")
        FINAL_NUMBER_OF_EACH_REGION=[float(i) for i in NUMBER_OF_EACH_REGION.split()]
        COLOR=simpledialog.askstring("input", "TYPE THE COLOUR OF EACH REGION SEPERATED BY SPACE")
        FINAL_COLOUR=[str(i) for i in COLOR.split()]
        plt.pie(FINAL_NUMBER_OF_EACH_REGION,labels=FINAL_REGIONS, autopct="%1.1f%%", colors=FINAL_COLOUR)
        plt.title(TITLE)
        plt.show()

    elif(GRAPHS==4):

        BAR_NAME=simpledialog.askstring("input", "TYPE THE NAME OF EACH BAR SEPERATED BY SPACE")
        FINAL_BAR_NAME=[str(i) for i in BAR_NAME.split()]
        EACH_BAR_VALUE=simpledialog.askstring("input", "TYPE THE VALUE OF EACH BAR SEPERATED BY SPACE")
        FINAL_EACH_BAR_VALUE=[float(i) for i in EACH_BAR_VALUE.split()]    
        COLOUR=simpledialog.askstring("input", "TYPE THE COLOR (MENTION ONE COLOUR)")
        X_LABEL=simpledialog.askstring("input","TYPE THE NAME OF X_AXIS ")
        Y_LABEL=simpledialog.askstring("input","TYPE THE NAME OF Y_AXIS ")
        TITLE=simpledialog.askstring("input","TYPE THE TITLE OF THE FIGURE ")
        LEGEND=simpledialog.askstring("input","TYPE THE NAME OF LEGEND ")
        plt.bar(FINAL_BAR_NAME, FINAL_EACH_BAR_VALUE , color=COLOUR, label=LEGEND) #bar for vertical barh for horizontal
        plt.xlabel(X_LABEL)
        plt.ylabel(Y_LABEL)
        plt.title(TITLE)
        plt.legend()
        plt.show()
    elif(GRAPHS==5):

        X=simpledialog.askstring("input", "ENTER THE VALUES OF X_AXIS")
        FINAL_X=[float(i) for i in X.split()]
        Y=simpledialog.askstring("input", "ENTER THE VALUES OF Y_AXIS")
        FINAL_Y=[float(i) for i in Y.split()]
        COLOUR=simpledialog.askstring("input", "TYPE THE COLOUR OF GRAPH")
        LABEL=simpledialog.askstring("input", "TYPE THE NAME OF LABEL")
        LINEWIDTH=simpledialog.askinteger("input", "TYPE THE LINEWIDTH")
        plt.plot(FINAL_X,FINAL_Y, color=COLOUR, linestyle="-", linewidth=LINEWIDTH, marker="o", label= LABEL)
        plt.grid(color=COLOUR, linestyle="-", linewidth=1)
        TITLE=simpledialog.askstring("input", "TYPE THE TITLE OF FIGURE")
        X_AXIS=simpledialog.askstring("input", "TYPE THE TITLE OF X_AXIS")
        Y_AXIS=simpledialog.askstring("input", "TYPE THE TITLE OF Y_AXIS")
        plt.xlabel(X_AXIS)
        plt.ylabel(Y_AXIS)
        plt.legend(loc="lower right", fontsize=12) #lower right left # upper right left
        plt.show()
def integration():



    INTEGRATION=simpledialog.askinteger("input","DO YOU WANT TO ADD LIMITS IN INTEGRATION EXPRESSION \n PRESS_1 FOR YES \n PRESS_2 FOR NO")
    
    
    if(INTEGRATION==1):
        
        X=sp.symbols("x")
        EX=simpledialog.askstring("input","PLEASE ENTER YOUR EXPRESSION FOR INTEGRATION \n DISCLAIMER ! \n USE THE VARIABLE SMALL x")
        simplified=sp.sympify(EX)


        UPPER_LIMIT=simpledialog.askfloat("input","TYPE THE VALUE OF UPPER_LIMIT ")
        LOWER_LIMIT=simpledialog.askfloat("input","TYPE THE VALUE OF LOWER_LIMIT ")        
        RESULT=sp.integrate(simplified, X)
        FINALL=(RESULT.subs(X, UPPER_LIMIT))-(RESULT.subs(X,LOWER_LIMIT))
        entry.delete(0, tk.END)
        entry.insert(0, str(FINALL))


    elif(INTEGRATION==2):
        X=sp.symbols("x")
        EXPRESSION=simpledialog.askstring("input","PLEASE ENTER YOUR EXPRESSION FOR INTEGRATION \n DISCLAIMER ! \n USE THE VARIABLE SMALL x")
        simplified=sp.sympify(EXPRESSION) #EXPRESSION is being read from input() as a string. SymPy requires a symbolic expression, not a string.
        RESULT=sp.integrate(simplified, X)
        entry.delete(0, tk.END)
        entry.insert(0, str(RESULT))

def log():
    input_value=float(entry.get())
    RESULT=math.log(input_value)
    entry.delete(0, tk.END)
    entry.insert(0, str(RESULT))

# ================= BUTTONS GUI =================

button_frame = tk.Frame(root)
button_frame.pack(pady=0, padx=0)

btn_font = ("arial", 19)
btn_w = 7
btn_h = 2

# -------- Trigonometric --------



tk.Button(button_frame, text="MATRICES", command=matrices, width=btn_w, height=btn_h,bg="grey").grid(row=0, column=0,)
tk.Button(button_frame, text="STATS", command=statistics, width=btn_w, height=btn_h,bg="grey").grid(row=0, column=1,)
tk.Button(button_frame, text="d/dx", command=differentiation, width=btn_w, height=btn_h,bg="grey").grid(row=0, column=2,)
tk.Button(button_frame, text="∫", command=integration, width=btn_w, height=btn_h,bg="grey").grid(row=0, column=3,)
tk.Button(button_frame, text="GRAPHS", command=graphs, width=btn_w, height=btn_h,bg="grey").grid(row=0, column=4,)
tk.Button(button_frame, text="ln", command=log, width=btn_w, height=btn_h,bg="grey").grid(row=0, column=5,)


tk.Button(button_frame, text="sin", command=sin, width=btn_w, height=btn_h,bg="grey").grid(row=4, column=0,)
tk.Button(button_frame, text="cos", command=cos, width=btn_w, height=btn_h,bg="grey").grid(row=4, column=1)
tk.Button(button_frame, text="tan", command=tan, width=btn_w, height=btn_h,bg="grey").grid(row=4, column=2)
tk.Button(button_frame, text="sec", command=sec, width=btn_w, height=btn_h,bg="grey").grid(row=4, column=3)
tk.Button(button_frame, text="cosec", command=cosec, width=btn_w, height=btn_h,bg="grey").grid(row=4, column=4)
tk.Button(button_frame, text="cot", command=cot, width=btn_w, height=btn_h,bg="grey").grid(row=4, column=5)
tk.Button(button_frame, text="sinh", command=sinh, width=btn_w, height=btn_h,bg="grey").grid(row=5, column=0)
tk.Button(button_frame, text="cosh", command=cosh, width=btn_w, height=btn_h,bg="grey").grid(row=5, column=1)
tk.Button(button_frame, text="tanh", command=tanh, width=btn_w, height=btn_h,bg="grey").grid(row=5, column=2)
tk.Button(button_frame, text="sech", command=sech, width=btn_w, height=btn_h,bg="grey").grid(row=5, column=3)
tk.Button(button_frame, text="cosech", command=cosech, width=btn_w, height=btn_h,bg="grey").grid(row=5, column=4)
tk.Button(button_frame, text="coth", command=coth, width=btn_w, height=btn_h,bg="grey").grid(row=5, column=5)


tk.Button(button_frame, text="sin⁻¹", command=arcsin, width=btn_w, height=btn_h,bg="grey").grid(row=6, column=0)
tk.Button(button_frame, text="cos⁻¹", command=arccos, width=btn_w, height=btn_h,bg="grey").grid(row=6, column=1)
tk.Button(button_frame, text="tan⁻¹", command=arctan, width=btn_w, height=btn_h,bg="grey").grid(row=6, column=2)
tk.Button(button_frame, text="sec⁻¹", command=arcsec, width=btn_w, height=btn_h,bg="grey").grid(row=6, column=3)
tk.Button(button_frame, text="cosec⁻¹", command=arccosec, width=btn_w, height=btn_h,bg="grey").grid(row=6, column=4)
tk.Button(button_frame, text="cot⁻¹", command=arccot, width=btn_w, height=btn_h,bg="grey").grid(row=6, column=5)

tk.Button(button_frame, text="sinh⁻¹", command=arcsinh, width=btn_w, height=btn_h,bg="grey").grid(row=7, column=0)
tk.Button(button_frame, text="cosh⁻¹", command=arccosh, width=btn_w, height=btn_h,bg="grey").grid(row=7, column=1)
tk.Button(button_frame, text="tanh⁻¹", command=arctanh, width=btn_w, height=btn_h,bg="grey").grid(row=7, column=2)
tk.Button(button_frame, text="sech⁻¹", command=arcsech, width=btn_w, height=btn_h,bg="grey").grid(row=7, column=3)
tk.Button(button_frame, text="cosech⁻¹", command=arccosech, width=btn_w, height=btn_h,bg="grey").grid(row=7, column=4)
tk.Button(button_frame, text="coth⁻¹", command=arccoth, width=btn_w, height=btn_h,bg="grey").grid(row=7, column=5)
tk.Button(button_frame, text="√", command=sqrt, width=btn_w, height=btn_h,bg="orange").grid(row=8, column=0)
tk.Button(button_frame, text="n!", command=factorial, width=btn_w, height=btn_h,bg="orange").grid(row=8, column=1)
tk.Button(button_frame, text="∛", command=cube_root, width=btn_w, height=btn_h,bg="orange").grid(row=8, column=2)
tk.Button(button_frame, text="x^y", command=X_power_Y, width=btn_w, height=btn_h,bg="orange").grid(row=8, column=3)
tk.Button(button_frame, text="nPr", command=permutation, width=btn_w, height=btn_h,bg="orange").grid(row=8, column=4)
tk.Button(button_frame, text="nCr", command=combination, width=btn_w, height=btn_h,bg="orange").grid(row=8, column=5)
tk.Button(button_frame, text="x^2", command=X_square, width=btn_w, height=btn_h,bg="lavender").grid(row=10, column=5)

tk.Button(button_frame, text="π", command=pi, width=btn_w, height=btn_h,bg="lavender", ).grid(row=9, column=5)

tk.Button(button_frame, text="=", width=btn_w, height=btn_h, bg="black",fg="white", command=calculate).grid(row=11, column=4)


tk.Button(button_frame, text="7", width=btn_w, height=btn_h, bg="Lavender", command=lambda: click("7")).grid(row=9, column=0)

tk.Button(button_frame, text="8", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("8")).grid(row=9, column=1)

tk.Button(button_frame, text="9", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("9")).grid(row=9, column=2)

tk.Button(button_frame, text="4", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("4")).grid(row=10, column=0)

tk.Button(button_frame, text="5", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("5")).grid(row=10, column=1)

tk.Button(button_frame, text="6", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("6")).grid(row=10, column=2)

tk.Button(button_frame, text="1", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("1")).grid(row=11, column=0)

tk.Button(button_frame, text="2", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("2")).grid(row=11, column=1)

tk.Button(button_frame, text="3", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("3")).grid(row=11, column=2)

tk.Button(button_frame, text="0", width=btn_w, height=btn_h,bg="Lavender", command=lambda: click("0")).grid(row=11, column=3)

tk.Button(button_frame, text="-", width=btn_w, height=btn_h, command=lambda: click("-"), bg="Lavender").grid(row=10, column=4)

tk.Button(button_frame, text="+", width=btn_w, height=btn_h, command=lambda: click("+"), bg="Lavender").grid(row=10, column=3)

tk.Button(button_frame, text="X", width=btn_w, height=btn_h, command=lambda: click("X"), bg="Lavender").grid(row=9, column=4)

tk.Button(button_frame, text="÷", width=btn_w, height=btn_h, command=lambda: click("÷"), bg="Lavender").grid(row=9, column=3)


tk.Button(button_frame, text="Clear", command=clear,
          width=btn_w, height=btn_h, bg="red", fg="black").grid(row=11, column=5)


root.mainloop()



