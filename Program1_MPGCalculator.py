# Naomi Puyleart
# 11/20/25
# MPG Calculator
# Write a GUI program that calculates a car's gas mileage.
# The program's window should have Entry widgets that let
# the user enter the number of gallons of gas the car holds,
# and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked, the program should
# display the number of miles that the car may be driven
# per gallon of gas.
# Use the following formula to calculate miles per gallon:
# MPG = miles / gallons.

import tkinter
import tkinter.messagebox

class MPGGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.title("MPG Calculator")

        # Frames
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)

        # Top widgets
        # Gallons
        self.gallons_label = tkinter.Label(self.top_frame, text='Enter the number of gallons of gas your car holds:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')


        # Miles
        self.miles_label = tkinter.Label(self.top_frame, text='Enter how many miles your car can be driven on a full tank of gas:')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')


        # Bottom widgets
        # Calculate button
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate_mpg)
        self.calc_button.pack(side='left')



        # Quit button
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit",
                                          command = self.window.destroy)
        self.quit_button.pack(side ='left')

        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()

    def calculate_mpg(self):
        gallons = self.gallons_entry.get()
        miles = self.miles_entry.get()
        mpg = float(miles) / float(gallons)
        tkinter.messagebox.showinfo("MPG", str(mpg) + " MPG")
        self.window.destroy()

if __name__ == "__main__":
    mpgGUI = MPGGUI()