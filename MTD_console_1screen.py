""" Mixed Tenure Development Console

The console for running the Mixed Tenure Development model as a stand-alone
program with user-specified inputs.

Author: Charles Peter Newland, SMEC
Email: charlesnewlandprofessional@outlook.com
Date of inception: 25/01/2019
Most recent update: 29/01/2019
"""

# STD library imports
from tkinter import *
from tkinter import filedialog
import xlwt

# 3rd party imports.

# Local modules.
# BROWSE BUTTON - Select output directory.
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def mtd_model():
    Levels = int(Lev.get())
    NetSellableArea = int(NSA.get())
    AreaPerLevel = NetSellableArea / Levels
    MixFormat = MF.get()

    # Unit sizing
    Bed1_size = float(B1S.get())
    Bed2S_size = float(B2SS.get())
    Bed2L_size = float(B2LS.get())
    Bed3_size = float(B3S.get())
    UnitCodes = ["B1", "B2S", "B2L", "B3"]
    UnitSizes = [Bed1_size, Bed2S_size, Bed2L_size, Bed3_size]
    # Unit location preference (Bottom, Middle, Top).
    Bed1_Pref = B1P.get()
    Bed2S_Pref = B2SP.get()
    Bed2L_Pref = B2LP.get()
    Bed3_Pref = B3P.get()
    UnitPrefs = [Bed1_Pref, Bed2S_Pref, Bed2L_Pref, Bed3_Pref]
    # Unit allocation.
    Bed1_Allocation = (Bed1_all_scale.get())/100
    Bed2S_Allocation = (Bed2S_all_scale.get())/100
    Bed2L_Allocation = (Bed2L_all_scale.get())/100
    Bed3_Allocation = (Bed3_all_scale.get())/100
    # Affordable housing unit allocation (percentage of total to be affordable).
    Bed1_AllocationAffordable = (Bed1_aa_scale.get())/100
    Bed2S_AllocationAffordable = (Bed2S_aa_scale.get())/100
    Bed2L_AllocationAffordable = (Bed2L_aa_scale.get())/100
    Bed3_AllocationAffordable = (Bed3_aa_scale.get())/100

    # Costing
    TotalValue = float(TV.get())
    PercentValueAffordable = PVA_scale.get()/100

    """PRELIMINARY APARTMENT SIZING CALCULATIONS"""
    # Floor space by apartment type.
    Bed1_TotalArea = NetSellableArea * Bed1_Allocation
    Bed2S_TotalArea = NetSellableArea * Bed2S_Allocation
    Bed2L_TotalArea = NetSellableArea * Bed2L_Allocation
    Bed3_TotalArea = NetSellableArea * Bed3_Allocation
    # Number of units by apartment type.
    Bed1_NoUnits = int(Bed1_TotalArea / Bed1_size)
    Bed2S_NoUnits = int(Bed2S_TotalArea / Bed2S_size)
    Bed2L_NoUnits = int(Bed2L_TotalArea / Bed2L_size)
    Bed3_NoUnits = int(Bed3_TotalArea / Bed3_size)
    # Number of affordable & private units by apartment type.
    Bed1_NoAffordableUnits = round(Bed1_NoUnits * Bed1_AllocationAffordable)
    Bed1_NoPrivateUnits = Bed1_NoUnits - Bed1_NoAffordableUnits
    Bed2S_NoAffordableUnits = round(Bed2S_NoUnits * Bed2S_AllocationAffordable)
    Bed2S_NoPrivateUnits = Bed2S_NoUnits - Bed2S_NoAffordableUnits
    Bed2L_NoAffordableUnits = round(Bed2L_NoUnits * Bed2L_AllocationAffordable)
    Bed2L_NoPrivateUnits = Bed2L_NoUnits - Bed2L_NoAffordableUnits
    Bed3_NoAffordableUnits = round(Bed3_NoUnits * Bed3_AllocationAffordable)
    Bed3_NoPrivateUnits = Bed3_NoUnits - Bed3_NoAffordableUnits

    NoPrivateUnits = Bed1_NoPrivateUnits + Bed2S_NoPrivateUnits \
                     + Bed2L_NoPrivateUnits + Bed3_NoPrivateUnits

    """PRELIMINARY COST CALCULATIONS"""
    ValuePerMetre = TotalValue / NetSellableArea
    UnitValues = [Bed1_size * ValuePerMetre, Bed2S_size * ValuePerMetre,
                  Bed2L_size * ValuePerMetre, Bed3_size * ValuePerMetre]

    """BUILDING GENERATION"""
    # Compile a list tracking the allocation of units.
    UnitTracker = [Bed1_NoUnits, Bed2S_NoUnits, Bed2L_NoUnits, Bed3_NoUnits]
    AffordableUnitTracker = [Bed1_NoAffordableUnits, Bed2S_NoAffordableUnits,
                             Bed2L_NoAffordableUnits, Bed3_NoAffordableUnits]
    # Allocate units to each floor.
    Building = {}
    # Use a list to track if the level is "full"
    LevelAreas = [AreaPerLevel] * Levels

    # First, allocate levels from the bottom floor up
    for i in range(0, Levels):
        # Generate a list to track the unit allocation per level by preference.
        Building[i + 1] = []
        # First, allocate one unit to each level based on preference.
        if i < Levels / 3:
            HeightCode = "Bottom"
            for j in range(0, len(UnitCodes)):
                if HeightCode == UnitPrefs[j]:
                    Building[i + 1].append(UnitCodes[j])
                    LevelAreas[i] = LevelAreas[i] - UnitSizes[j]
                    UnitTracker[j] = UnitTracker[j] - 1
                else:
                    pass
        elif i > 2 / 3 * Levels:
            HeightCode = "Top"
            for j in range(0, len(UnitCodes)):
                if HeightCode == UnitPrefs[j]:
                    Building[i + 1].append(UnitCodes[j])
                    LevelAreas[i] = LevelAreas[i] - UnitSizes[j]
                    UnitTracker[j] = UnitTracker[j] - 1
                else:
                    pass
        else:
            HeightCode = "Middle"
            for j in range(0, len(UnitCodes)):
                if HeightCode == UnitPrefs[j]:
                    Building[i + 1].append(UnitCodes[j])
                    LevelAreas[i] = LevelAreas[i] - UnitSizes[j]
                    UnitTracker[j] = UnitTracker[j] - 1
                else:
                    pass
    # With units allocated by preference to certain heights, these are copied
    # across to fill out each level (if possible) from the top down.
    for i in range(Levels - 1, 0, -1):
        # Preference unit code.
        PrefUnitLayout = Building[i + 1]
        indexes = []
        # Find the index(es).
        for j in range(0, len(PrefUnitLayout)):
            dummy = UnitCodes.index(PrefUnitLayout[j])
            indexes.append(dummy)
        # With the index values, now copy across.
        RemainingUnits = 0
        for j in range(0, len(indexes)):
            RemainingUnits = RemainingUnits + UnitTracker[indexes[j]]
        # Now iterate through and allocate Units.
        while LevelAreas[i] > max(UnitSizes) and RemainingUnits > 0:
            for j in range(0, len(indexes)):
                Building[i + 1].append(UnitCodes[indexes[j]])
                LevelAreas[i] = LevelAreas[i] - UnitSizes[indexes[j]]
                UnitTracker[indexes[j]] = UnitTracker[indexes[j]] - 1
                RemainingUnits = RemainingUnits - 1

    # Allocate the remaining units where possible.
    CurrentLevel = 0
    while CurrentLevel < Levels:
        while LevelAreas[CurrentLevel] > max(UnitSizes):
            # Add units sequentially until space is violated.
            for i in range(0, len(UnitCodes)):
                if UnitTracker[i] > 0 and LevelAreas[CurrentLevel] - UnitSizes[i] >= 0:
                    Building[CurrentLevel + 1].append(UnitCodes[i])
                    LevelAreas[CurrentLevel] = LevelAreas[CurrentLevel] - UnitSizes[i]
                    UnitTracker[i] = UnitTracker[i] - 1
        CurrentLevel += 1

    # Allocate additional units where possible.
    for i in range(0, Levels):
        if LevelAreas[i] < min(UnitSizes):
            pass
        else:
            for j in range(len(UnitCodes) - 1, -1, -1):
                if LevelAreas[i] - UnitSizes[j] >= 0:
                    Building[i + 1].append(UnitCodes[j])
                    LevelAreas[i] = LevelAreas[i] - UnitSizes[j]

    # Now, allocate affordable housing as required.
    for i in range(0, Levels):
        if MixFormat == "Partial Mix":
            for j in range(0, len(Building[i + 1])):
                UnitType = Building[i + 1][j]
                dummy = UnitCodes.index(UnitType)
                if AffordableUnitTracker[dummy] > 0:
                    # If an affordable unit add a prefix to show.
                    Building[i + 1][j] = "A_" + Building[i + 1][j]
                    AffordableUnitTracker[dummy] -= 1
        elif MixFormat == "Salt & Pepper":
            MixTrack = [0] * len(UnitCodes)
            for j in range(0, len(Building[i + 1])):
                UnitType = Building[i + 1][j]
                dummy = UnitCodes.index(UnitType)
                if MixTrack[dummy] == 0 and AffordableUnitTracker[dummy] > 0:
                    # If an affordable unit add a prefix to show.
                    Building[i + 1][j] = "A_" + Building[i + 1][j]
                    AffordableUnitTracker[dummy] -= 1
                    MixTrack[dummy] = 1
                elif MixTrack[dummy] == 1:
                    MixTrack[dummy] = 0

    """COST CALCULATION"""
    ValuePerAffordableLot = [i * PercentValueAffordable for i in UnitValues]
    AffordableUnitTracker = [Bed1_NoAffordableUnits, Bed2S_NoAffordableUnits,
                             Bed2L_NoAffordableUnits, Bed3_NoAffordableUnits]
    TotalValueAffordableLots = 0

    for i in range(0, len(ValuePerAffordableLot)):
        TotalValueAffordableLots = TotalValueAffordableLots + \
                                   ValuePerAffordableLot[i] \
                                   * AffordableUnitTracker[i]
    # Cost calculations for private lots.
    TotalValuePrivateLots = TotalValue - TotalValueAffordableLots
    TotalPrivateLotArea = Bed1_NoPrivateUnits * Bed1_size \
                          + Bed2S_NoPrivateUnits * Bed2S_size \
                          + Bed2L_NoPrivateUnits * Bed2L_size \
                          + Bed3_NoPrivateUnits * Bed3_size

    ValuePerMetrePrivate = TotalValuePrivateLots / TotalPrivateLotArea
    ValuePerPrivateLot = [i * ValuePerMetrePrivate for i in UnitSizes]

    """PRINT BUILDING"""
    bg_cols = ["#FAFAFA", "#C8C8C8", "#969696", "#646464"]
    xminrel = 0.55
    xmaxrel = 0.95
    yminrel = 0.20
    ymaxrel = 0.90

    max_bld_width = 75
    max_bld_height = 32

    # Determine the level height. Rounded down to nearest integer.
    level_height = int(max_bld_height / Levels)

    # Determine the relative position of each level in the
    # y plane. Go from the top down.
    y_level_pos = [0] * (Levels + 1)
    for i in range(Levels, 0, -1):
        y_level_pos[i] = yminrel + (Levels - i) \
                         * (ymaxrel - yminrel) / Levels

    # Determine the relative space and pixel width each unit
    # occupies in the x plane.
    unit_pxl_pos = [0] * len(UnitCodes)
    unit_pxl_size = [0] * len(UnitCodes)
    for i in range(0, len(UnitCodes)):
        unit_pxl_pos[i] = UnitSizes[i] / AreaPerLevel * \
                          (xmaxrel - xminrel)
        unit_pxl_size[i] = UnitSizes[i] / AreaPerLevel * max_bld_width

    for i in range(Levels, 0, -1):
        # First, set a full width label with an indent.
        Label(MTDConsole, relief=SUNKEN, width=75,
              height=level_height).place(relx=xminrel, rely=y_level_pos[i])
        # Initialise a parameter to track the x position.
        x_pos = xminrel
        # Next, iterate through and insert the different units.
        for j in range(0, len(Building[i])):
            lbl_txt = Building[i][j]
            # Find the unit code index.
            unit_idx = 0
            if "B3" in lbl_txt:
                unit_idx = 3
            elif "B2L" in lbl_txt:
                unit_idx = 2
            elif "B2S" in lbl_txt:
                unit_idx = 1
            else:
                unit_idx = 0
            lbl_col = bg_cols[unit_idx]
            unit_width = int(unit_pxl_size[unit_idx])
            # Draw the label.
            Label(MTDConsole, bg=lbl_col, width=unit_width,
                  height=level_height, borderwidth=1,
                  relief="solid", text=lbl_txt).place(
                relx=x_pos, rely=y_level_pos[i]
            )
            # Finally, update x_pos.
            x_pos = x_pos + unit_pxl_pos[unit_idx]

    # Save output
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("New_Building", cell_overwrite_ok=True)
    # Specify formats for excel writing.
    fmt_pr = "pattern: pattern solid, fore_colour gray25;" \
             "borders: top thin, bottom thin;"
    fmt_af = "pattern: pattern solid, fore_colour gray50;" \
             "borders: top thin, bottom thin;"
    # Iterate through the dictionary to write the level by level output (goes
    # from the top down.
    for i in range(1, Levels + 1):
        sheet1.write((Levels + 1) - i, 0, "Level " + str(i),
                     xlwt.Style.easyxf("borders: top thin, bottom thin;"))
        for j in range(0, len(Building[i])):
            if "A_" in Building[i][j]:
                sheet1.write((Levels + 1) - i, j + 1, Building[i][j],
                             xlwt.Style.easyxf(fmt_af))
            else:
                sheet1.write((Levels + 1) - i, j + 1, Building[i][j],
                             xlwt.Style.easyxf(fmt_pr))

    # Extract teh final row value.
    final_row = i
    # Now write the costing value.
    sheet1.write(final_row + 3, 0, "Value per Assisted Lot:")
    sheet1.write(final_row + 4, 0, "Value per Private Lot:")
    for i in range(0, len(UnitCodes)):
        sheet1.write(final_row + 2, i + 1, UnitCodes[i])
        sheet1.write(final_row + 3, i + 1, ValuePerAffordableLot[i])
        sheet1.write(final_row + 4, i + 1, ValuePerPrivateLot[i])

    # Save the output.
    XL_name = StringVar()
    XL_name = "//output.xlsx"
    OutputXLName = folder_path + XL_name
    book.save(OutputXLName)

    return

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

# Variable declaration.
# Ouptut path
folder_path = StringVar()
# Apartment building inputs
Lev = StringVar()
NSA = StringVar()
TV = StringVar()
PVA = StringVar()

# Unit Codes.
UnitCodes = ["B1", "B2S", "B2L", "B3"]
# Unit sizing (NSA square metres).
B1S = StringVar()
B2SS = StringVar()
B2LS = StringVar()
B3S = StringVar()
# Unit allocation (percentage of building for each unit type).
B1A = StringVar()
B2SA = StringVar()
B2LA = StringVar()
B3A = StringVar()
# Affordable housing unit allocation (percentage of total to be affordable).
B1AA = StringVar()
B2SAA = StringVar()
B2LAA = StringVar()
B3AA = StringVar()


# BUILDING PARAMETERS
BP_label = Label(text="Building Settings", font=H_txt, justify=CENTER)
BP_label.place(relx=0.15, rely=0.05, anchor=N)
# Number of levels.
NoLev_label = Label(text="Number of levels:", font=B_txt)
NoLev_label.place(relx=0, rely=0.10, anchor=W)
NoLev_entry = Entry(textvariable=Lev)
NoLev_entry.place(relx=0.14, rely=0.10, anchor=W, width=50)
# Net Sellable Area.
NSA_label = Label(text="Total Net Sellable Area (NSA):", font=B_txt)
NSA_label.place(relx=0, rely=0.14, anchor=W)
NSA_entry = Entry(textvariable=NSA)
NSA_entry.place(relx=0.14, rely=0.14, anchor=W, width=50)
# Total Value.
TV_label = Label(text="Total Value ($):", font=B_txt)
TV_label.place(relx=0, rely=0.18, anchor=W)
TV_entry = Entry(textvariable=TV)
TV_entry.place(relx=0.14, rely=0.18, anchor=W, width=50)
# Options Menu - Preference.
MF_label = Label(text="Mixture Format:", font=B_txt)
MF_label.place(relx=0, rely=0.22, anchor=W)
MF = StringVar()
MF_entry = OptionMenu(MTDConsole, MF, "Salt & Pepper", "Partial Mix")
MF_entry.place(relx=0.12, rely=0.22, anchor=W, width=125)
# Percentage value of affordable housing
PVA_label = Label(text="Percentage value\n of affordable housing (%):")
PVA_label.place(relx=0, rely=0.27, anchor=W)
PVA_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
PVA_scale.place(relx=0.13, rely=0.27, anchor=W, width=150)


# UNIT INPUTS
# Heading Label
US_label = Label(text="Unit Settings", font=H_txt, justify=CENTER)
US_label.place(relx=0.15, rely=0.30, anchor=N)
# Size label
Size_label = Label(text="NSA (sq. m)")
Size_label.place(relx=0.15, rely=0.35, anchor=N)
# Allocation label
All_label = Label(text="Allocation (%)*")
All_label.place(relx=0.25, rely=0.35, anchor=N)
# Allocation % Note Label.
note_label = Label(text="* Must sum to 100%", font=N_txt)
note_label.place(relx=0.25, rely=0.38, anchor=N)
# Preference label
Pref_label = Label(text="Preference")
Pref_label.place(relx=0.375, rely=0.35, anchor=N)
# 1 Bedroom label, unit info
Bed1_label = Label(text="1 Bedroom:", font=B_txt)
Bed1_label.place(relx=0, rely=0.45, anchor=W)
# 2 Bedroom Standard label, unit info
Bed2S_label = Label(text="2 Bedroom Standard:", font=B_txt)
Bed2S_label.place(relx=0, rely=0.50, anchor=W)
# 2 Bedroom Large label, unit info
Bed2L_label = Label(text="2 Bedroom Large:", font=B_txt)
Bed2L_label.place(relx=0, rely=0.55, anchor=W)
# 3 Bedroom label, unit info
Bed3_label = Label(text="3 Bedroom:", font=B_txt)
Bed3_label.place(relx=0, rely=0.60, anchor=W)

# 1 Bedroom NSA entry.
Bed1_size_entry = Entry(textvariable=B1S)
Bed1_size_entry.place(relx=0.14, rely=0.45, anchor=W, width=50)
# 2 Bedroom Standard NSA entry.
Bed2S_size_entry = Entry(textvariable=B2SS)
Bed2S_size_entry.place(relx=0.14, rely=0.50, anchor=W, width=50)
# 2 Bedroom Large NSA entry.
Bed2L_size_entry = Entry(textvariable=B2LS)
Bed2L_size_entry.place(relx=0.14, rely=0.55, anchor=W, width=50)
# 3 Bedroom NSA entry.
Bed3_size_entry = Entry(textvariable=B3S)
Bed3_size_entry.place(relx=0.14, rely=0.60, anchor=W, width=50)
# 1 Bedroom allocation slider
Bed1_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed1_all_scale.place(relx=0.20, rely=0.45, anchor=W, width=150)
# 2 Bedroom Standard allocation slider
Bed2S_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2S_all_scale.place(relx=0.20, rely=0.50, anchor=W, width=150)
# 2 Bedroom Large allocation slider
Bed2L_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2L_all_scale.place(relx=0.20, rely=0.55, anchor=W, width=150)
# 3 Bedroom allocation slider
Bed3_all_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed3_all_scale.place(relx=0.20, rely=0.60, anchor=W, width=150)
# 1 Bedroom height preference option menu
B1P = StringVar()
Bed1_pref_entry = OptionMenu(MTDConsole, B1P, "Bottom", "Middle", "Top",
                             "None")
Bed1_pref_entry.place(relx=0.33, rely=0.45, anchor=W, width=100)
# 2 Bedroom Standard height preference option menu
B2SP = StringVar()
Bed2S_pref_entry = OptionMenu(MTDConsole, B2SP, "Bottom", "Middle",
                              "Top", "None")
Bed2S_pref_entry.place(relx=0.33, rely=0.50, anchor=W, width=100)
# 2 Bedroom Large height preference option menu
B2LP = StringVar()
Bed2L_pref_entry = OptionMenu(MTDConsole, B2LP, "Bottom", "Middle",
                              "Top", "None")
Bed2L_pref_entry.place(relx=0.33, rely=0.55, anchor=W, width=100)
# 3 Bedroom height preference option menu
B3P = StringVar()
Bed3_pref_entry = OptionMenu(MTDConsole, B3P, "Bottom", "Middle", "Top",
                             "None")
Bed3_pref_entry.place(relx=0.33, rely=0.60, anchor=W, width=100)

# AFFORDABILITY INPUTS
AFF_label = Label(text="Affordability Settings", font=H_txt, justify=CENTER)
AFF_label.place(relx=0.15, rely=0.65, anchor=N)
# Affordability allocation label.
Aff_All_label = Label(text="Affordable Allocation of Units (%)")
Aff_All_label.place(relx=0.15, rely=0.68, anchor=N)
# 1 Bedroom label, affordability
Bed1_label = Label(text="1 Bedroom:", font=B_txt)
Bed1_label.place(relx=0, rely=0.75, anchor=W)
# 2 Bedroom Standard label, affordability
Bed2S_label = Label(text="2 Bedroom Standard:", font=B_txt)
Bed2S_label.place(relx=0, rely=0.80, anchor=W)
# 2 Bedroom Large label, affordability
Bed2L_label = Label(text="2 Bedroom Large:", font=B_txt)
Bed2L_label.place(relx=0, rely=0.85, anchor=W)
# 3 Bedroom label, affordability
Bed3_label = Label(text="3 Bedroom:", font=B_txt)
Bed3_label.place(relx=0, rely=0.90, anchor=W)

# 1 Bedroom Scale bar, affordability allocation.
Bed1_aa_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed1_aa_scale.place(relx=0.12, rely=0.75, anchor=W, width=150)
# 2 Bedroom Standard Scale bar, , affordability allocation.
Bed2S_aa_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2S_aa_scale.place(relx=0.12, rely=0.80, anchor=W, width=150)
# 2 Bedroom Large Scale bar, affordability allocation.
Bed2L_aa_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed2L_aa_scale.place(relx=0.12, rely=0.85, anchor=W, width=150)
# 3 Bedroom Scale bar, affordability allocation.
Bed3_aa_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
Bed3_aa_scale.place(relx=0.12, rely=0.90, anchor=W, width=150)

# RUN BUTTON
run_btn = Button(MTDConsole, text='Run', command=mtd_model)
run_btn.place(relx=0.5, rely=0.0, anchor=N)

# OUTPUTS
# Output label.
output_label = Label(text="Output", font=H_txt)
output_label.place(relx=0.75, rely=0.05)

save_label = Label(text="Select output directory:")
save_label.place(relx=0.62, rely=0.1)
save_button = Button(text="Browse", command=browse_button, textvariable=folder_path)
save_button.place(relx=0.75, rely=0.1)

# Run the console.
MTDConsole.mainloop()
