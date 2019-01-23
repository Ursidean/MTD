""" Mixed Tenure Development Console

The console for running the Mixed Tenure Development model as a stand-alone
program with user-specified inputs.

Author: Charles Peter Newland, SMEC
Email: charlesnewlandprofessional@outlook.com
Date of inception: 23/01/2019
Most recent update: 23/01/2019
"""

# STD library imports
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure

# 3rd party imports.


# Local modules.

# Disclaimer message.
DisclaimerText = "Welcome to the Mixed Tenure Development Model. This model " \
                 "is used to generate the layout of a mixed tenure apartment" \
                 " building based on user inputs." \
                 ""


"""Graphical User Interface"""
# Font styles, Heading(H), Body(B)
H_txt = ("Arial", 12)
B_txt = ("Arial", 10)

# Generate the figure that will be plotted.
f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

# MTD Console GUI
class MTDConsole(tk.Tk):
    """Mixed Tenure Development Model Console
    Base console for the Graphical User Interface (GUI) that store the
    different pages used by the model and
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        # Add icon.
        tk.Tk.iconbitmap(self, default="SMEC_Logo.ico")
        # Add title text.
        tk.Tk.wm_title(self, "Mixed Tenure Demand Model")

        # Add containers (program windows).
        container = tk.Frame(self)
        # Configuration of window.
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to store frames for each window.
        self.frames = {}
        # Iterate through frames to initialize. Must be included in tuple to
        # work.
        for F in (StartPage, InputPg1):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    """Start Page.
    The starting page of the Mixed Tenure Development Application.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=200)
        label = tk.Label(self, text="Start Page", font=H_txt)
        label.place(relx=0.5, rely=0.0, anchor=tk.N)
        # Disclaimer relief.
        disclaimer = ttk.Label(self, text=DisclaimerText, relief=tk.SUNKEN,
                               wraplength=300)
        disclaimer.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Start button.
        button1 = ttk.Button(self, text="Start",
                             command=lambda: controller.show_frame(InputPg1))
        button1.place(relx=0.0, rely=1.0, anchor=tk.SW)
        # Quit button.
        quit_button = ttk.Button(self, text="Quit", command=quit)
        quit_button.place(relx=1.0, rely=1.0, anchor=tk.SE)

class InputPg1(tk.Frame):
    """Input page 1
    Takes the building inputs.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Input Page 1", font=H_txt)
        label.pack(pady=10, padx=10)

        # Entry box.

        # Back button.

        # Quit button.
        quit_button = ttk.Button(self, text="Quit", command=quit)
        quit_button.pack()


# Run the application.
app = MTDConsole()
app.mainloop()
