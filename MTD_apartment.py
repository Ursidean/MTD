"""Mixed Tenure Development Model - Apartment build
Program for design of a Mixed Tenure Development apartment block. User can
provide a range of inputs and the program will design an apartment building
meeting the specifications outlined.

Copyright: Charles Peter Newland, SMEC
Date of inception: 09/01/2019
Most recent update: 09/01/2019

"""

# STD library imports

# 3rd party library imports
import xlwt

# Local module imports

"""INPUTS"""
# Apartment building inputs
Levels = 20
NetSellableArea = 10000
AreaPerLevel = NetSellableArea/Levels
PerAffordableUnits = 0.40
# Unit sizing (NSA square metres).
Bed1_size = 65
Bed2S_size = 75
Bed2L_size = 90
Bed3_size = 100
UnitCodes = ["B1", "B2S", "B2L", "B3"]
UnitSizes = [Bed1_size, Bed2S_size, Bed2L_size, Bed3_size]
# Unit location preference (Bottom, Middle, Top).
Bed1_Pref = "Bottom"
Bed2S_Pref = "Middle"
Bed2L_Pref = "Middle"
Bed3_Pref = "Top"
UnitPrefs = [Bed1_Pref, Bed2S_Pref, Bed2L_Pref, Bed3_Pref]
# Unit allocation (percentage of building for each unit type).
Bed1_Allocation = 0.20
Bed2S_Allocation = 0.35
Bed2L_Allocation = 0.35
Bed3_Allocation = 0.10
# Affordable housing unit allocation (percentage of total to be affordable).
Bed1_AllocationAffordable = 0.50
Bed2S_AllocationAffordable = 0.50
Bed2L_AllocationAffordable = 0.0
Bed3_AllocationAffordable = 0.0

# Set the mixture format as either Salt & Pepper, Partial Mix, or Segregated.
MixFormat = "Salt & Pepper"

# Preference factors. Either "Private" or "Affordable".
PrefHeight = "Private"
PrefRetail = "Private"

# Costing
TotalValue = 10000000
PercentValueAffordable = 0.50

"""PRELIMINARY APARTMENT SIZING CALCULATIONS"""
# Floor space by apartment type.
Bed1_TotalArea = NetSellableArea * Bed1_Allocation
Bed2S_TotalArea = NetSellableArea * Bed2S_Allocation
Bed2L_TotalArea = NetSellableArea * Bed2L_Allocation
Bed3_TotalArea = NetSellableArea * Bed3_Allocation
# Number of units by apartment type.
Bed1_NoUnits = int(Bed1_TotalArea/Bed1_size)
Bed2S_NoUnits = int(Bed2S_TotalArea/Bed2S_size)
Bed2L_NoUnits = int(Bed2L_TotalArea/Bed2L_size)
Bed3_NoUnits = int(Bed3_TotalArea/Bed3_size)
# Number of affordable & private units by apartment type.
Bed1_NoAffordableUnits = round(Bed1_NoUnits * Bed1_AllocationAffordable)
Bed1_NoPrivateUnits = Bed1_NoUnits - Bed1_NoAffordableUnits
Bed2S_NoAffordableUnits = round(Bed2S_NoUnits * Bed2S_AllocationAffordable)
Bed2S_NoPrivateUnits = Bed2S_NoUnits - Bed2S_NoAffordableUnits
Bed2L_NoAffordableUnits = round(Bed2L_NoUnits * Bed2L_AllocationAffordable)
Bed2L_NoPrivateUnits = Bed2L_NoUnits - Bed2L_NoAffordableUnits
Bed3_NoAffordableUnits = round(Bed3_NoUnits * Bed3_AllocationAffordable)
Bed3_NoPrivateUnits = Bed3_NoUnits - Bed3_NoAffordableUnits

"""PRELIMINARY COST CALCULATIONS"""
ValuePerMetre = TotalValue/NetSellableArea

"""BUILDING GENERATION"""
# Compile a list tracking the allocation of units.
UnitTracker = [Bed1_NoUnits, Bed2S_NoUnits, Bed2L_NoUnits, Bed3_NoUnits]
# Allocate units to each floor.
Building = {}
# Use a list to track if the level is "full"
LevelAreas = [AreaPerLevel] * Levels
# First, allocate levels from the bottom floor up
for i in range(0, Levels):
    # Generate a list to track the unit allocation per level by preference.
    Building[i + 1] = []
    # First, allocate one unit to each level based on preference.
    if i < Levels/3:
        HeightCode = "Bottom"
        for j in range(0, len(UnitCodes)):
            if HeightCode == UnitPrefs[j]:
                Building[i + 1].append(UnitCodes[j])
                LevelAreas[i] = LevelAreas[i] - UnitSizes[j]
                UnitTracker[j] = UnitTracker[j] - 1
            else:
                pass
    elif i > 2/3 * Levels:
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
Floor = Levels



print(Building)






"""
## BUILDING GENERATTION

# Generate the building for each level.
Building = {}
for i in range(1, Levels + 1):
    Building[i] = ["P"] * int(LotsPerLevel)

# Allocate affordable apartments to each level.
AffordableLotCounter = 0
# Track the code of the previous lot allocation.
PreviousLot = "P"
# Iterate through the build and allocate
if PrefHeight == "Affordable":
    # If the height preference is for affordable housing, iterate from the
    # top-down.
    for i in range(Levels, 0, -1):
        for j in range(0, LotsPerLevel):
            # Allocation for segregated design.
            if MixFormat == "Segregated":
                if AffordableLotCounter == int(NoAffordableLots):
                    break
                else:
                    Building[i][j] = "A"
                    AffordableLotCounter += 1
            # Allocation for Salt & Pepper design.
            elif MixFormat == "Salt & Pepper":
                if AffordableLotCounter == int(NoAffordableLots):
                    break
                elif PreviousLot == "A":
                    Building[i][j] = "P"
                    PreviousLot = "P"
                else:
                    Building[i][j] = "A"
                    PreviousLot = "A"
                    AffordableLotCounter += 1

elif PrefHeight == "Private":
    # If the height preference if for private housing, iterate from the
    # bottom-up.
    for i in range(1, Levels + 1):
        for j in range(0, LotsPerLevel):
            # Allocation for segregated design.
            if MixFormat == "Segregated":
                if AffordableLotCounter == int(NoAffordableLots):
                    break
                else:
                    Building[i][j] = "A"
                    AffordableLotCounter += 1
            elif MixFormat == "Salt & Pepper":
                if AffordableLotCounter == int(NoAffordableLots):
                    break
                elif PreviousLot == "A":
                    Building[i][j] = "P"
                    PreviousLot = "P"
                else:
                    Building[i][j] = "A"
                    PreviousLot = "A"
                    AffordableLotCounter += 1

# Cost calculations.
ValuePerAffordableLot = ValuePerLot * PercentValueAffordable
TotalValueAffordableLots = ValuePerAffordableLot * NoAffordableLots
TotalValuePrivateLots = TotalValue - TotalValueAffordableLots
ValuePerPrivateLot = TotalValuePrivateLots/NoPrivateLots



## OUTPUTS
# Write the output to an Excel workbook. First specify a new workbook.
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
        if Building[i][j] == "P":
            sheet1.write((Levels + 1) - i, j + 1, "Private", xlwt.Style.easyxf(fmt_pr))
        elif Building[i][j] == "A":
            sheet1.write((Levels + 1) - i, j + 1, "Assisted", xlwt.Style.easyxf(fmt_af))
# Extract teh final row value.
final_row = i
# Now write the costing value.
sheet1.write(final_row + 2, 0, "Value per Assisted Lot:")
sheet1.write(final_row + 2, 1, ValuePerAffordableLot)
sheet1.write(final_row + 3, 0, "Value per Private Lot:")
sheet1.write(final_row + 3, 1, ValuePerPrivateLot)
# Save the output.
OutputDirectory = "C:\\Users\\CN14439\\PycharmProjects\\MTD\\MTD_A_output\\"
OutputXLName = OutputDirectory + "output.xls"
book.save(OutputXLName)
"""