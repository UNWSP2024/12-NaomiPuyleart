# Naomi Puyleart
# 11/20/25
# Joe's Automotive
# Joe's Automotive performs the following routine
# maintenance service:
#
# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to
# select any or all of these services.
# When the user clicks a button, the total charges should
# be displayed.

# This program demonstrates a group of Checkbutton widgets.

import tkinter
import tkinter.messagebox

class AutomotiveGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler replacement - $200.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.cb_var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Display button
        self.display_button = tkinter.Button(self.bottom_frame, text='Display Total Price', command=self.total_price)
        self.display_button.pack(side='left')

        # Quit button
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit",
                                          command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def total_price(self):
        self.message = 'Your total price is: $'
        total = 0
        if self.cb_var1.get() == 1:
            total += 30.00
        if self.cb_var2.get() == 1:
            total += 20.00
        if self.cb_var3.get() == 1:
            total += 40.00
        if self.cb_var4.get() == 1:
            total += 100.00
        if self.cb_var5.get() == 1:
            total += 35.00
        if self.cb_var6.get() == 1:
            total += 200.00
        if self.cb_var7.get() == 1:
            total += 20.00

        self.message += str(total)

        tkinter.messagebox.showinfo('Total Price', self.message)



if __name__ == "__main__":
    automotiveGUI = AutomotiveGUI()