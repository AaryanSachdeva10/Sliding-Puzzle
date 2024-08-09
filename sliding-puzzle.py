# Created by Aaryan Sachdeva on 11/07/2023

from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Sliding Puzzle Game")
root.geometry("380x435")
root.resizable(False, False)
root.iconbitmap("C:/Users/Manish/Desktop/Aaryan stuff/Python coding/Images/slider.ico")

amount_of_turns = 0

button_1 = Button(root, text="1",font=('Helvetica', 50), width=3, height=1, command=lambda: button_click(button_1))
button_2 = Button(root, text="2",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_2))
button_3 = Button(root, text="3",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_3))
button_4 = Button(root, text="4",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_4))
button_5 = Button(root, text="5",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_5))
button_6 = Button(root, text="6",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_6))
button_7 = Button(root, text="7",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_7))
button_8 = Button(root, text="8",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_8))
button_9 = Button(root, text="9",font=('Helvetica', 50), width=3, height=1,command=lambda: button_click(button_9))
empty = Button(root, text="  ",font=('Helvetica', 50), width=3, height=1, state=DISABLED)

turns = Label(root, text="Turns: " + str(amount_of_turns))
turns.place(x=170, y=394)

def button_click(button):
	row_diff = abs(empty.grid_info()['row'] - button.grid_info()['row'])
	col_diff = abs(empty.grid_info()['column'] - button.grid_info()['column'])

	if row_diff == 1 and col_diff == 0 or row_diff == 0 and col_diff == 1:
			buttonrow = button.grid_info()["row"]
			emptyrow = empty.grid_info()["row"]

			buttoncolumn = button.grid_info()["column"]
			emptycolumn = empty.grid_info()["column"]

			emptyrow,buttonrow = buttonrow, emptyrow
			emptycolumn,buttoncolumn = buttoncolumn,emptycolumn

			empty.grid(row=emptyrow, column=emptycolumn)
			button.grid(row=buttonrow, column=buttoncolumn)

			global amount_of_turns
			amount_of_turns+=1

			turns.config(text="Turns: " + str(amount_of_turns))
			check_if_ended()

def check_if_ended():
	if button_1.grid_info()['row'] == 0 and button_1.grid_info()['column'] == 0 and button_2.grid_info()['row'] == 0 and button_2.grid_info()['column'] == 1 and button_3.grid_info()['row'] == 0 and button_3.grid_info()['column'] == 2 and button_4.grid_info()['row'] == 1 and button_4.grid_info()['column'] == 0 and button_5.grid_info()['row'] == 1 and button_5.grid_info()['column'] == 1 and button_6.grid_info()['row'] == 1 and button_6.grid_info()['column'] == 2 and button_7.grid_info()['row'] == 2 and button_7.grid_info()['column'] == 0 and button_8.grid_info()['row'] == 2 and button_8.grid_info()['column'] == 1:
		mb = messagebox.askyesno("Sliding Puzzle Game", "Game Ended. Well Done! It took you " + str(amount_of_turns) + " turns to complete the puzzle. Do you want to play again?")
		if mb > 0:
			reset()

def reset():
	random_array_row = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
	random_grid = []
	random_split = []
	i = 0
	global amount_of_turns
	amount_of_turns = 0
	turns.config(text="Turns: " + str(amount_of_turns))

	while i != 9:
		randomgrid = random.choice(random_array_row)
		random_grid.append(randomgrid)
		random_array_row.remove(randomgrid)
		randomgrid = random_grid[0]
		i+=1

	for value in random_grid:
		digits = [int(digit) for digit in str(value)]
		random_split.extend(digits)

	button_1.grid(row=random_split[0], column=random_split[1])
	button_2.grid(row=random_split[2], column=random_split[3])
	button_3.grid(row=random_split[4], column=random_split[5])
	button_4.grid(row=random_split[6], column=random_split[7])
	button_5.grid(row=random_split[8], column=random_split[9])
	button_6.grid(row=random_split[10], column=random_split[11])
	button_7.grid(row=random_split[12], column=random_split[13])
	button_8.grid(row=random_split[14], column=random_split[15])
	button_9.grid_remove()

	empty.grid(row=random_split[16], column=random_split[17])

def quit():
	mb = messagebox.askyesno("Quit Game", "Are you sure you want to quit?")
	if mb > 0:
		root.destroy()

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
space = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
my_menu.add_cascade(label="                  Created by Aaryan Sachdeva", menu=space, state=DISABLED)
options_menu.add_command(label="Reset Game", command=reset)
options_menu.add_command(label="Quit Game", command=quit)

reset()

root.mainloop()