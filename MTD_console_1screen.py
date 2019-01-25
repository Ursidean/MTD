""" Mixed Tenure Development Console

The console for running the Mixed Tenure Development model as a stand-alone
program with user-specified inputs.

Author: Charles Peter Newland, SMEC
Email: charlesnewlandprofessional@outlook.com
Date of inception: 25/01/2019
Most recent update: 25/01/2019
"""

# STD library imports
import math
from tkinter import *
from tkinter import ttk
# 3rd party imports.

# Local modules.


def mtd_model():
    Levels = float(Lev)
    NetSellableArea = float(NSA)
    AreaPerLevel = NetSellableArea / Levels
    # Unit sizing
    Bed1_size = float(B1S)
    Bed2S_size = float(B2SS)
    Bed2L_size = float(B2LS)
    Bed3_size = float(B3S)
    UnitSizes = [Bed1_size, Bed2S_size, Bed2L_size, Bed3_size]
    # Unit allocation.
    Bed1_Allocation = 0.20
    Bed2S_Allocation = 0.35
    Bed2L_Allocation = 0.35
    Bed3_Allocation = 0.10




    return

# VARIABLE DECLARATION.
# Apartment building inputs
Lev = StringVar()
NSA = StringVar()
# Unit Codes.
UnitCodes = ["B1", "B2S", "B2L", "B3"]
# Unit sizing (NSA square metres).
B1S = StringVar()
B2SS = StringVar()
B2LS = StringVar()
B3S = StringVar()
# Unit allocation (percentage of building for each unit type).
Bed1_Allocation = StringVar()
Bed2S_Allocation = StringVar()
Bed2L_Allocation = StringVar()
Bed3_Allocation = StringVar()
# Affordable housing unit allocation (percentage of total to be affordable).
Bed1_AllocationAffordable = StringVar()
Bed2S_AllocationAffordable = StringVar()
Bed2L_AllocationAffordable = StringVar()
Bed3_AllocationAffordable = StringVar()


# BASES
# Initialise Mixed Tenure Demand Model Window.
MTDConsole = Tk()
# Add title
MTDConsole.title("Mixed Tenure Demand Model")
# Add icon.
MTDConsole.iconbitmap(default="SMEC_Logo.ico")
# Size the window to the size of the screen.
screen_width = MTDConsole.winfo_screenwidth()
screen_height = MTDConsole.winfo_screenwidth()
# res = str(screen_width) + "x" + str(screen_height)
MTDConsole.geometry("%dx%d+0+0" % (screen_width, screen_height))
# Font styles, Heading(H), Body(B), Note(N).
H_txt = ("Arial", 12)
B_txt = ("Arial", 10)
N_txt = ("Arial", 7)

# BUILDING PARAMETERS
BP_label = Label(text="Building Settings", font=H_txt, justify=CENTER)
BP_label.place(relx=0.15, rely=0.05, anchor=N)
# Number of levels.
NoLev_label = Label(text="Number of levels:", font=B_txt)
NoLev_label.place(relx=0, rely=0.10, anchor=W)
NoLev_entry = Entry()
NoLev_entry.place(relx=0.14, rely=0.10, anchor=W, width=50)
# Net Sellable Area.
NSA_label = Label(text="Total Net Sellable Area (NSA):", font=B_txt)
NSA_label.place(relx=0, rely=0.14, anchor=W)
NSA_entry = Entry()
NSA_entry.place(relx=0.14, rely=0.14, anchor=W, width=50)
# Total Value.
TV_label = Label(text="Total Value ($):", font=B_txt)
TV_label.place(relx=0, rely=0.18, anchor=W)
TV_entry = Entry()
TV_entry.place(relx=0.14, rely=0.18, anchor=W, width=50)
# Options Menu - Preference.
MF_label = Label(text="Mixture Format:", font=B_txt)
MF_label.place(relx=0, rely=0.22, anchor=W)
MixFormat = StringVar()
MF_entry = OptionMenu(MTDConsole, MixFormat, "Salt & Pepper", "Partial Mix")
MF_entry.place(relx=0.12, rely=0.22, anchor=W, width=125)

# UNIT INPUTS
# Heading Label
US_label = Label(text="Unit Settings", font=H_txt, justify=CENTER)
US_label.place(relx=0.15, rely=0.30, anchor=N)
# Size label
Size_label = Label(text="NSA (sq. m)")
Size_label.place(relx=0.15, rely=0.35, anchor=N)
# Allocation label
All_label = Label(text="Allocation (%)*")
All_label.place(relx=0.23, rely=0.35, anchor=N)
# Allocation % Note Label.
note_label = Label(text="* Must sum to 100%", font=N_txt)
note_label.place(relx=0.23, rely=0.54, anchor=N)
# Preference label
Pref_label = Label(text="Preference")
Pref_label.place(relx=0.31, rely=0.35, anchor=N)
# 1 Bedroom label, unit info
Bed1_label = Label(text="1 Bedroom:", font=B_txt)
Bed1_label.place(relx=0, rely=0.40, anchor=W)
# 2 Bedroom Standard label, unit info
Bed2S_label = Label(text="2 Bedroom Standard:", font=B_txt)
Bed2S_label.place(relx=0, rely=0.44, anchor=W)
# 2 Bedroom Large label, unit info
Bed2L_label = Label(text="2 Bedroom Large:", font=B_txt)
Bed2L_label.place(relx=0, rely=0.48, anchor=W)
# 3 Bedroom label, unit info
Bed3_label = Label(text="3 Bedroom:", font=B_txt)
Bed3_label.place(relx=0, rely=0.52, anchor=W)

# 1 Bedroom NSA entry.
Bed1_size_entry = Entry(textvariable=Bed1_size)
Bed1_size_entry.place(relx=0.14, rely=0.40, anchor=W, width=50)
# 2 Bedroom Standard NSA entry.
Bed2S_size_entry = Entry(textvariable=Bed2S_size)
Bed2S_size_entry.place(relx=0.14, rely=0.44, anchor=W, width=50)
# 2 Bedroom Large NSA entry.
Bed2L_size_entry = Entry(textvariable=Bed2L_size)
Bed2L_size_entry.place(relx=0.14, rely=0.48, anchor=W, width=50)
# 3 Bedroom NSA entry.
Bed3_size_entry = Entry(textvariable=Bed3_size)
Bed3_size_entry.place(relx=0.14, rely=0.52, anchor=W, width=50)
# 1 Bedroom allocation slider
Bed1_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed1_all_scale.place(relx=0.20, rely=0.40, anchor=W, width=125)
# 2 Bedroom Standard allocation slider
Bed2S_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2S_all_scale.place(relx=0.20, rely=0.44, anchor=W, width=125)
# 2 Bedroom Large allocation slider
Bed2L_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2L_all_scale.place(relx=0.20, rely=0.48, anchor=W, width=125)
# 3 Bedroom allocation slider
Bed3_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed3_all_scale.place(relx=0.20, rely=0.52, anchor=W, width=125)
# 1 Bedroom height preference option menu
Bed1_Pref = StringVar()
Bed1_pref_entry = OptionMenu(MTDConsole, Bed1_Pref, "Bottom", "Middle", "Top",
                             "None", textvariable=Bed1_Pref)
Bed1_pref_entry.place(relx=0.28, rely=0.40, anchor=W, width=100)
# 2 Bedroom Standard height preference option menu
Bed2S_Pref = StringVar()
Bed2S_pref_entry = OptionMenu(MTDConsole, Bed2S_Pref, "Bottom", "Middle",
                              "Top", "None", textvariable=Bed2S_Pref)
Bed2S_pref_entry.place(relx=0.28, rely=0.44, anchor=W, width=100)
# 2 Bedroom Large height preference option menu
Bed2L_Pref = StringVar()
Bed2L_pref_entry = OptionMenu(MTDConsole, Bed2L_Pref, "Bottom", "Middle",
                              "Top", "None", textvariable=Bed2L_Pref)
Bed2L_pref_entry.place(relx=0.28, rely=0.48, anchor=W, width=100)
# 3 Bedroom height preference option menu
Bed3_Pref = StringVar()
Bed3_pref_entry = OptionMenu(MTDConsole, Bed3_Pref, "Bottom", "Middle", "Top",
                             "None", textvariable=Bed3_Pref)
Bed3_pref_entry.place(relx=0.28, rely=0.52, anchor=W, width=100)

# AFFORDABILITY INPUTS
AFF_label = Label(text="Affordability Settings", font=H_txt, justify=CENTER)
AFF_label.place(relx=0.15, rely=0.60, anchor=N)
# Affordability allocation label.
Aff_All_label = Label(text="Affordable Allocation of Units (%)")
Aff_All_label.place(relx=0.15, rely=0.63, anchor=N)
# 1 Bedroom label, affordability
Bed1_label = Label(text="1 Bedroom:", font=B_txt)
Bed1_label.place(relx=0, rely=0.68, anchor=W)
# 2 Bedroom Standard label, affordability
Bed2S_label = Label(text="2 Bedroom Standard:", font=B_txt)
Bed2S_label.place(relx=0, rely=0.72, anchor=W)
# 2 Bedroom Large label, affordability
Bed2L_label = Label(text="2 Bedroom Large:", font=B_txt)
Bed2L_label.place(relx=0, rely=0.76, anchor=W)
# 3 Bedroom label, affordability
Bed3_label = Label(text="3 Bedroom:", font=B_txt)
Bed3_label.place(relx=0, rely=0.80, anchor=W)

# 1 Bedroom Scale bar, affordability.
Bed1_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed1_scale.place(relx=0.12, rely=0.68, anchor=W, width=125)
# 2 Bedroom Standard Scale bar, affordability.
Bed2S_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2S_scale.place(relx=0.12, rely=0.72, anchor=W, width=125)
# 2 Bedroom Large Scale bar, affordability.
Bed2L_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2L_scale.place(relx=0.12, rely=0.76, anchor=W, width=125)
# 3 Bedroom Scale bar.
Bed3_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed3_scale.place(relx=0.12, rely=0.80, anchor=W, width=125)



# Run the console.
MTDConsole.mainloop()


"""
main = Tk()
main.title("How Much?")
main.geometry('300x300')

amount = StringVar()
intRate = StringVar()
years = StringVar()

lblAmount = Label(main, text='Amount of Purchase:').grid(row=0, column=0,
                                                         padx=0, pady=10)
entAmount = Entry(main, textvariable=amount).grid(row=0, column=1)

lblIntRate = Label(main, text='Interest Rate (like 7.5):').grid(row=1,
                                                                column=0,
                                                                padx=0,
                                                                pady=10)
entIntRate = Entry(main, textvariable=intRate).grid(row=1, column=1)

lblYears = Label(main, text='Years to Pay:').grid(row=2, column=0, padx=0,
                                                  pady=10)
entYears = Entry(main, textvariable=years).grid(row=2, column=1)

btn = Button(main, text='Calculate', command=calculatePayment).grid(row=5,
                                                                    column=1)

lblMonthly = Label(main, text='Monthly Payment:').grid(row=3, column=0, padx=0,
                                                       pady=10)
lblTotal = Label(main, text='Total Purchase Cost:').grid(row=4, column=0,
                                                         padx=0, pady=10)

main.mainloop()
"""