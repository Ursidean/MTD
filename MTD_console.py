""" Mixed Tenure Development Console

The console for running the Mixed Tenure Development model as a stand-alone
program with user-specified inputs.

Author: Charles Peter Newland, SMEC
Email: charlesnewlandprofessional@outlook.com
Date of inception: 23/01/2019
Most recent update: 25/01/2019
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
# Global variable declaration.

# Unit Codes.
UnitCodes = ["B1", "B2S", "B2L", "B3"]
# Unit sizing
Bed1_size = ""
Bed2S_size = ""
Bed2L_size = ""
Bed3_size = ""
# Unit allocation (percentage of building for each unit type).
# Bed1_Allocation = ""
# Bed2S_Allocation = ""
# Bed2L_Allocation = ""
# Bed3_Allocation = ""
# Affordable housing unit allocation (percentage of total to be affordable).
Bed1_AllocationAffordable = ""
Bed2S_AllocationAffordable = ""
Bed2L_AllocationAffordable = ""
Bed3_AllocationAffordable = ""
# Costing
TotalValue = ""
PercentValueAffordable = 0.50


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
        for F in (StartPage, InputPg1, InputPg2, InputPg3, ModelPg):
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
        tk.Frame.__init__(self, parent, width=600, height=350)
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
        label = tk.Label(self, text="Building Input Page", font=H_txt)
        label.pack(pady=10, padx=10)
        # Entry box - Number of levels.
        NoLev_label = tk.Label(self, text="Number of levels:", font=B_txt)
        NoLev_label.place(relx=0, rely=0.25, anchor=tk.W)
        NoLev_entry = tk.Entry(self)
        NoLev_entry.place(relx=0.50, rely=0.25, anchor=tk.W, width=150)
        # Entry box - Net Sellable Area.
        NSA_label = tk.Label(self, text="Total Net Sellable Area (NSA):", font=B_txt)
        NSA_label.place(relx=0, rely=0.35, anchor=tk.W)
        NSA_entry = tk.Entry(self)
        NSA_entry.place(relx=0.50, rely=0.35, anchor=tk.W, width=150)
        # Entry box - Total Value.
        TV_label = tk.Label(self, text="Total Value ($):", font=B_txt)
        TV_label.place(relx=0, rely=0.45, anchor=tk.W)
        TV_entry = tk.Entry(self)
        TV_entry.place(relx=0.50, rely=0.45, anchor=tk.W, width=150)
        # Options Menu - Preference.
        MF_label = tk.Label(self, text="Mixture Format:", font=B_txt)
        MF_label.place(relx=0, rely=0.55, anchor=tk.W)
        MixFormat = tk.StringVar()
        MF_entry = tk.OptionMenu(self, MixFormat, "Salt & Pepper", "Partial Mix")
        MF_entry.place(relx=0.50, rely=0.55, anchor=tk.W, width=150)

        # Next button.
        next_button = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame(InputPg2)
        )
        next_button.place(relx=0.0, rely=1.0, anchor=tk.SW)
        # Back button.
        back_button = ttk.Button(
            self, text="Back",
            command=lambda: controller.show_frame(StartPage)
        )
        back_button.place(relx=0.5, rely=1.0, anchor=tk.S)
        # Quit button.
        quit_button = ttk.Button(self, text="Quit", command=quit)
        quit_button.place(relx=1.0, rely=1.0, anchor=tk.SE)


class InputPg2(tk.Frame):
    """Input page 2
    Take the room size inputs.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # LABELS
        label = tk.Label(self, text="Unit Inputs Page", font=H_txt)
        label.pack(pady=10, padx=10)
        # Size label
        Size_label = tk.Label(self, text="NSA (sq. m)")
        Size_label.place(relx=0.35, rely=0.10, anchor=tk.N)
        # Allocation label
        All_label = tk.Label(self, text="Allocation (%)")
        All_label.place(relx=0.60, rely=0.10, anchor=tk.N)
        # Allocation note
        All_note = tk.Label(self, text="*Note, these must sum to 100%",
                            font=B_txt)
        All_note.place(relx=0.60, rely=0.75, anchor=tk.S)
        # Preference label
        Pref_label = tk.Label(self, text="Preference")
        Pref_label.place(relx=0.85, rely=0.10, anchor=tk.N)
        # 1 Bedroom label
        Bed1_label = tk.Label(self, text="1 Bedroom:", font=B_txt)
        Bed1_label.place(relx=0, rely=0.25, anchor=tk.W)
        # 2 Bedroom Standard label
        Bed2S_label = tk.Label(self, text="2 Bedroom Standard:", font=B_txt)
        Bed2S_label.place(relx=0, rely=0.35, anchor=tk.W)
        # 2 Bedroom Large label
        Bed2L_label = tk.Label(self, text="2 Bedroom Large:", font=B_txt)
        Bed2L_label.place(relx=0, rely=0.45, anchor=tk.W)
        # 3 Bedroom label
        Bed3_label = tk.Label(self, text="3 Bedroom:", font=B_txt)
        Bed3_label.place(relx=0, rely=0.55, anchor=tk.W)

        # ENTRY BOXES - Unit size
        # 1 Bedroom
        Bed1_size_entry = tk.Entry(self, textvariable=Bed1_size)
        Bed1_size_entry.place(relx=0.30, rely=0.25, anchor=tk.W, width=50)
        # 2 Bedroom Standard
        Bed2S_size_entry = tk.Entry(self, textvariable=Bed2S_size)
        Bed2S_size_entry.place(relx=0.30, rely=0.35, anchor=tk.W, width=50)
        # 2 Bedroom Large
        Bed2L_size_entry = tk.Entry(self, textvariable=Bed2L_size)
        Bed2L_size_entry.place(relx=0.30, rely=0.45, anchor=tk.W, width=50)
        # 3 Bedroom
        Bed3_size_entry = tk.Entry(self, textvariable=Bed3_size)
        Bed3_size_entry.place(relx=0.30, rely=0.55, anchor=tk.W, width=50)

        # ENTRY BOXES - Unit percentage allocation
        # 1 Bedroom
        Bed1_all_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed1_all_scale.place(relx=0.45, rely=0.22, anchor=tk.W, width=150)
        # 2 Bedroom Standard
        Bed2S_all_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed2S_all_scale.place(relx=0.45, rely=0.32, anchor=tk.W, width=150)
        # 2 Bedroom Large
        Bed2L_all_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed2L_all_scale.place(relx=0.45, rely=0.42, anchor=tk.W, width=150)
        # 3 Bedroom
        Bed3_all_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed3_all_scale.place(relx=0.45, rely=0.52, anchor=tk.W, width=150)

        Bed1_Allocation = (Bed1_all_scale.get())/100
        Bed2S_Allocation = (Bed2S_all_scale.get())/100
        Bed2L_Allocation = (Bed2L_all_scale.get())/100
        Bed3_Allocation = (Bed3_all_scale.get())/100


        # SELECTION BOXES - Unit height preference
        # 1 Bedroom
        Bed1_Pref = tk.StringVar()
        Bed1_pref_entry = tk.OptionMenu(self, Bed1_Pref, "Bottom", "Middle", "Top", "None")
        Bed1_pref_entry.place(relx=0.80, rely=0.25, anchor=tk.W, width=100)
        # 2 Bedroom Standard
        Bed2S_Pref = tk.StringVar()
        Bed2S_pref_entry = tk.OptionMenu(self, Bed2S_Pref, "Bottom", "Middle", "Top", "None")
        Bed2S_pref_entry.place(relx=0.80, rely=0.35, anchor=tk.W, width=100)
        # 2 Bedroom Large
        Bed2L_Pref = tk.StringVar()
        Bed2L_pref_entry = tk.OptionMenu(self, Bed2L_Pref, "Bottom", "Middle", "Top", "None")
        Bed2L_pref_entry.place(relx=0.80, rely=0.45, anchor=tk.W, width=100)
        # 3 Bedroom
        Bed3_Pref = tk.StringVar()
        Bed3_pref_entry = tk.OptionMenu(self, Bed3_Pref, "Bottom", "Middle", "Top", "None")
        Bed3_pref_entry.place(relx=0.80, rely=0.55, anchor=tk.W, width=100)

        # Next button.
        next_button = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame(InputPg3)
        )
        next_button.place(relx=0.0, rely=1.0, anchor=tk.SW)
        # Back button.
        back_button = ttk.Button(
            self, text="Back",
            command=lambda: controller.show_frame(InputPg1)
        )
        back_button.place(relx=0.5, rely=1.0, anchor=tk.S)
        # Quit button.
        quit_button = ttk.Button(self, text="Quit", command=quit)
        quit_button.place(relx=1.0, rely=1.0, anchor=tk.SE)


class InputPg3(tk.Frame):
    """Input page 3
    Take the affordable housing inputs.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # LABELS
        label = tk.Label(self, text="Affordability Settings Input Page", font=H_txt)
        label.pack(pady=10, padx=10)
        # 1 Bedroom label
        Bed1_label = tk.Label(self, text="1 Bedroom:", font=B_txt)
        Bed1_label.place(relx=0, rely=0.25, anchor=tk.W)
        # 2 Bedroom Standard label
        Bed2S_label = tk.Label(self, text="2 Bedroom Standard:", font=B_txt)
        Bed2S_label.place(relx=0, rely=0.35, anchor=tk.W)
        # 2 Bedroom Large label
        Bed2L_label = tk.Label(self, text="2 Bedroom Large:", font=B_txt)
        Bed2L_label.place(relx=0, rely=0.45, anchor=tk.W)
        # 3 Bedroom label
        Bed3_label = tk.Label(self, text="3 Bedroom:", font=B_txt)
        Bed3_label.place(relx=0, rely=0.55, anchor=tk.W)


        # SCALE BARS
        # 1 Bedroom Scale bar.
        Bed1_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed1_scale.place(relx=0.40, rely=0.25, anchor=tk.W, width=150)
        # 2 Bedroom Standard Scale bar.
        Bed2S_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed2S_scale.place(relx=0.40, rely=0.35, anchor=tk.W, width=150)
        # 2 Bedroom Large Scale bar.
        Bed2L_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed2L_scale.place(relx=0.40, rely=0.45, anchor=tk.W, width=150)
        # 3 Bedroom Scale bar.
        Bed3_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        Bed3_scale.place(relx=0.40, rely=0.55, anchor=tk.W, width=150)
        # Run button.
        run_button = ttk.Button(
            self, text="Run Model", command=lambda: controller.show_frame(ModelPg)
        )
        run_button.place(relx=0.0, rely=1.0, anchor=tk.SW)
        # Back button.
        back_button = ttk.Button(
            self, text="Back",
            command=lambda: controller.show_frame(InputPg2)
        )
        back_button.place(relx=0.5, rely=1.0, anchor=tk.S)
        # Quit button.
        quit_button = ttk.Button(self, text="Quit", command=quit)
        quit_button.place(relx=1.0, rely=1.0, anchor=tk.SE)


class ModelPg(tk.Frame):
    """Input page 3
    Take the affordable housing inputs.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Entry
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        # Button
        b = tk.Button(self, text="okay", command=printtext())
        b.pack(side=tk.BOTTOM)


# Run the application.
app = MTDConsole()
app.mainloop()
