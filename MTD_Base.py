"""Mixed Tenure Development Model
Program for modelling Mixed Tenure Developments. The user inputs a zoning
plan for a new suburb and can develop scenarios for the proposed development
based on the attraction of different factors and the desired financial
output.
"""

# STD library imports
import numpy as np
import os
import sys
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
    NavigationToolbar2TkAgg
from matplotlib.figure import Figure


# 3rd party library imports

# Local module imports

"""Import data."""
"""
# Zoning map.
user_input_zone_map_path = input("Enter the full path of your file: ")
# Check whether the file is found.
assert os.path.exists(user_input_zone_map_path), \
    "File not found at: " + str(user_input_zone_map_path)

zone_map = np.loadtxt(user_input_zone_map_path)
print("File located and loaded.")
"""

# Equivalent code.
base_path = dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = base_path + "\\Data\\"
zone_map = np.loadtxt(data_path + "example_data.txt")


"""Graphical User Interface"""
# Font styles, Heading(H), Body(B)
H_txt = ("Arial", 12)
B_txt = ("Arial", 10)


# Mixed Tenure Development Application (MxdTenDevGUI).
class MxdTenDevApp(tk.Tk):
    """

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
        for F in (StartPage, PageOne, PageTwo, PageThree):
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
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=H_txt)
        label.pack(pady=10, padx=10)
        # Start page button 1.
        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()
        # Start page button 2.
        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        # Start page button 3.
        button3 = ttk.Button(self, text="Visit Page 3",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    """Page one.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1", font=H_txt)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Go to Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    """Page Two.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", font=H_txt)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):
    """Page Three.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=H_txt)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        # Generate the figure that will be plotted.
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6], [5, 6, 3, 4, 8, 1])
        # Canvas is used to show the figure in the Tkinter window.
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # Add a toolbar for navigating the Matplotlib Figure.
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




"""Run the Application."""
app = MxdTenDevApp()
app.mainloop()
