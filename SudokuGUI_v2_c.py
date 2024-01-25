from tkinter import *
import Sudoku_v0
import SimAnn_v2
import numpy as np
import random

difficulty = None

# Function to set the selected difficulty level
def set_difficulty(level):
    global difficulty
    difficulty = level

# Function to create the difficulty selection window
def create_difficulty_selection_window():
    window = Tk()
    window.title("Select Difficulty")
    
    # Buttons for different difficulty levels
    Button(window, text="Easy", command=lambda: [window.destroy(), set_difficulty("Easy"), start_Sudoku()]).pack()
    Button(window, text="Medium", command=lambda: [window.destroy(), set_difficulty("Medium"), start_Sudoku()]).pack()
    Button(window, text="INSANE", command=lambda: [window.destroy(), set_difficulty("INSANE"), start_Sudoku()]).pack()
    
    window.mainloop()
    print(difficulty)

# Function to start the Sudoku game for Easy difficulty
def start_Sudoku():
    if difficulty == "Easy":
        root= Tk()
        root.title("Sudoku Solver")
        root.geometry("420x600")
        
        # Function to validate the input in Sudoku cells
        def ValidateNumber(P):
            out = (P.isdigit() or P =="") and len(P) < 2
            return out

        reg = root.register(ValidateNumber)
        
        cells= {}
        
        sdk = Sudoku_v0.Sudoku(9)
        
        sdk.init_config()
        
        sdk_not_solved = sdk.copy()
        
        # Run the simulated annealing algorithm until convergence
        while SimAnn_v2.converge[0] == False:
            sdk.init_config()
            best = SimAnn_v2.simann(sdk, mcmc_steps=10**4, seed=58473625, beta0=1.0, anneal_steps=10)
        
        np.set_printoptions(threshold=np.inf) # force numpy to print the whole table
        
        # Function to draw a 3x3 grid of Sudoku cells
        def draw3x3Grid(row, column, bgcolor):
            for i in range(3):
                for j in range(3):
                    e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
                    e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
                    cells[(row+i+1, column+j+1)] = e

        # Function to draw a 9x9 grid of Sudoku cells
        def draw9x9Grid():
            color = "#D0ffff"
            for rowNo in range(1,10,3):
                for colNo in range(0,9,3):
                    draw3x3Grid(rowNo, colNo, color)
                    if color == "#D0ffff":
                        color = "#ffffd0"
                    else:
                        color = "#D0ffff"

        # Function to clear the values in the Sudoku cells
        def clearValues():
            for row in range(2,11):
                for col in range(1,10):
                    cell = cells[(row,col)]
                    cell.delete(0, "end")

        # Function to initialize the values in the Sudoku cells with random numbers
        def initValues():
            for rows in range(2,11):
                for col in range(1,10):
                    p = random.randint(1,9)
                    cells[(rows, col)].delete(0, "end")
                    if p == 1 or p == 2 or p ==3 or p == 4:
                        cells[(rows, col)].insert(0, best.table[rows - 2][col - 1])

        # Function to get the values from the best solution and update the Sudoku cells
        def getValues():
            for rows in range(2,11):
                for col in range(1,10):
                    cells[(rows, col)].delete(0, "end")
                    cells[(rows, col)].insert(0, best.table[rows - 2][col - 1])

        # Create buttons for starting, clearing, and solving the Sudoku game
        btn = Button(root, command=initValues, text="Start", width=10)
        btn.grid(row=25, column=3, columnspan=5, pady=20)

        btn = Button(root, command=clearValues, text="Clear", width=10)
        btn.grid(row=20, column=1, columnspan=5, pady=20)

        btn = Button(root, command=getValues, text="Solve", width=10)
        btn.grid(row=20, column=5, columnspan=5, pady=20)

        # Draw the 9x9 grid of Sudoku cells
        draw9x9Grid()
        root.mainloop()
        
    # Function to start the Sudoku game for INSANE difficulty
    elif difficulty == "INSANE":
        root = Tk()
        root.title("Sudoku Solver")
        root.geometry("2400x4000")
        
        # Define a function to validate the input number in the Sudoku cells
        def ValidateNumber(P):
            out = (P.isdigit() or P =="") and len(P) < 3
            return out

        # Register the validation function with Tkinter
        reg = root.register(ValidateNumber)

        # Create a dictionary to store the Sudoku cells
        cells = {}

        # Create a Sudoku object with size 25x25
        sdk = Sudoku_v0.Sudoku(25)

        # Initialize the Sudoku configuration
        sdk.init_config()

        # Create a copy of the Sudoku object for unsolved Sudoku
        sdk_not_solved = sdk.copy()

        # Run the simulated annealing algorithm until convergence
        while SimAnn_v2.converge[0] == False:
            sdk.init_config()
            best = SimAnn_v2.simann(sdk, mcmc_steps=10**4, seed=58473625, beta0=1.0, anneal_steps=40)

        # Set numpy print options to print the whole table
        np.set_printoptions(threshold=np.inf)

        # Define a function to draw a 5x5 grid of Sudoku cells
        def draw5x5Grid(row, column, bgcolor):
            for i in range(5):
                for j in range(5):
                    e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
                    e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
                    cells[(row+i+1, column+j+1)] = e

        # Define a function to draw a 25x25 grid of Sudoku cells
        def draw25x25Grid():
            color = "#D0ffff"
            for rowNo in range(1,26,5):
                for colNo in range(0,25,5):
                    draw5x5Grid(rowNo, colNo, color)
                    if color == "#D0ffff":
                        color = "#ffffd0"
                    else:
                        color = "#D0ffff"

        # Define a function to clear the values in the Sudoku cells
        def clearValues():
            for row in range(2,27):
                for col in range(1,26):
                    cell = cells[(row,col)]
                    cell.delete(0, "end")


        # Define function to initialize values in Sudoku cells
        def initValues():
            for rows in range(2, 27):
                for col in range(1, 26):
                    p = random.randint(1, 2)
                    cells[(rows, col)].delete(0, "end")
                    if p == 1:
                        cells[(rows, col)].insert(0, best.table[rows - 2][col - 1])

        # Define function to get values from the solution and update Sudoku cells
        def getValues():
            for rows in range(2, 27):
                for col in range(1, 26):
                    cells[(rows, col)].delete(0, "end")
                    cells[(rows, col)].insert(0, best.table[rows - 2][col - 1])

        # Create "Start" button
        btn = Button(root, command=initValues, text="Start", width=10)
        btn.grid(row=23, column=33, columnspan=5, padx=10)

        # Create "Clear" button
        btn = Button(root, command=clearValues, text="Clear", width=10)
        btn.grid(row=20, column=36, columnspan=5, padx=10)

        # Create "Solve" button
        btn = Button(root, command=getValues, text="Solve", width=10)
        btn.grid(row=20, column=30, columnspan=5, padx=10)

        # Draw the 25x25 grid of Sudoku cells
        draw25x25Grid()

        # Run the main event loop
        root.mainloop()

        # If difficulty is "Medium"
    elif difficulty == "Medium":
            root = Tk()
            root.title("Sudoku Solver")
            root.geometry("735x900")

            # Define function to validate input number
            def ValidateNumber(P):
                out = (P.isdigit() or P == "") and len(P) < 3
                return out

            reg = root.register(ValidateNumber)

            cells = {}

            sdk = Sudoku_v0.Sudoku(16)

            sdk.init_config()

            sdk_not_solved = sdk.copy()

            while SimAnn_v2.converge[0] == False:
                sdk.init_config()
                best = SimAnn_v2.simann(sdk, mcmc_steps=10**4, seed=58473625, beta0=1.0, anneal_steps=10)

            np.set_printoptions(threshold=np.inf)  # Force numpy to print the whole table

            # Define function to draw a 4x4 grid of Sudoku cells
            def draw4x4Grid(row, column, bgcolor):
                for i in range(4):
                    for j in range(4):
                        e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
                        e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
                        cells[(row+i+1, column+j+1)] = e

            # Define function to draw a 16x16 grid of Sudoku cells
            def draw16x16Grid():
                for rowNo in range(1, 17, 4):
                    if rowNo == 5 or rowNo == 13:
                        color = "#ffffd0"
                    else:
                        color = "#D0ffff"

                    for colNo in range(0, 16, 4):
                        draw4x4Grid(rowNo, colNo, color)

                        if color == "#D0ffff":
                            color = "#ffffd0"
                        else:
                            color = "#D0ffff"

            # Define function to clear the values in the Sudoku cells
            def clearValues():
                for row in range(2, 18):
                    for col in range(1, 17):
                        cell = cells[(row, col)]
                        cell.delete(0, "end")

    
            # Function to initialize values in Sudoku cells
            def initValues():
                for rows in range(2, 18):
                    for col in range(1, 17):
                        p = random.randint(1, 11)
                        cells[(rows, col)].delete(0, "end")
                        if p in [1, 2, 3, 4, 5]:
                            cells[(rows, col)].insert(0, best.table[rows - 2][col - 1])
    
            # Function to get values from the solution and update Sudoku cells
            def getValues():
                for rows in range(2, 18):
                    for col in range(1, 17):
                        cells[(rows, col)].delete(0, "end")
                        cells[(rows, col)].insert(0, best.table[rows - 2][col - 1])
    
            # Create "Start" button
            btn = Button(root, command=initValues, text="Start", width=10)
            btn.grid(row=25, column=7, columnspan=5, pady=20)
    
            # Create "Clear" button
            btn = Button(root, command=clearValues, text="Clear", width=10)
            btn.grid(row=20, column=5, columnspan=5, pady=20)
    
            # Create "Solve" button
            btn = Button(root, command=getValues, text="Solve", width=10)
            btn.grid(row=20, column=9, columnspan=5, pady=20)
    
            # Draw the 16x16 grid of Sudoku cells
            draw16x16Grid()

            # Run the main event loop
            root.mainloop()

# Call function to create difficulty selection window
create_difficulty_selection_window()

