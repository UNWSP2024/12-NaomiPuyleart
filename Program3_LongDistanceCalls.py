# Naomi Puyleart
# 11/20/25
# Long Distance Calls
# A long-distance provider charges the following rates
# for telephone calls:
#
# Rate Category                         Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
# Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
# Off-Peak (midnight through 5:59 P.M.) 	$0.05
#
# Write a GUI application that allows the user to select
# a rate category (from a set of radio buttons),
# and enter the number of minutes of the call into an Entry widget.
# An info dialog box should display the charge for the call.

import tkinter
import tkinter.messagebox

class CallsGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Label
        self.rate_label = tkinter.Label(self.top_frame, text="Rate Category - Rate per Minute")
        self.rate_label.pack()

        # Radiobuttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text="Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02", variable = self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text="Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12", variable = self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text="Off-Peak (midnight through 5:59 P.M.) 	$0.05", variable = self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Minutes
        self.minutes_label = tkinter.Label(self.top_frame, text='Enter the number of minutes you would like to call:')
        self.minutes_entry = tkinter.Entry(self.top_frame, width=10)

        self.minutes_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        # Display button
        self.display_button = tkinter.Button(self.bottom_frame, text='Display Total Charge', command=self.display)
        self.display_button.pack(side='left')

        # Quit button
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit",
                                          command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def display(self):
        total = 0
        if self.radio_var.get() == 1:
            total += float(self.minutes_entry.get()) * .02
        if self.radio_var.get() == 2:
            total += float(self.minutes_entry.get()) * .12
        if self.radio_var.get() == 3:
            total += float(self.minutes_entry.get()) * 0.05
        self.message = "Your total charge is: $" + str(f"{total:.2f}")
        tkinter.messagebox.showinfo('Total Charge', self.message)




if __name__ == "__main__":
    callsGUI = CallsGUI()