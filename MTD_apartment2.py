"""Mixed Tenure Development Model - Apartment build
Program for design of a Mixed Tenure Development apartment block. User can
provide a range of inputs and the program will design an apartment building
meeting the specifications outlined.

Author: Charles Peter Newland, SMEC
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

# Set the mixture format as either Salt & Pepper or Partial Mix.
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

NoPrivateUnits = Bed1_NoPrivateUnits + Bed2S_NoPrivateUnits \
                 + Bed2L_NoPrivateUnits + Bed3_NoPrivateUnits

"""PRELIMINARY COST CALCULATIONS"""
ValuePerMetre = TotalValue/NetSellableArea
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


ValuePerMetrePrivate = TotalValuePrivateLots/TotalPrivateLotArea
ValuePerPrivateLot = [i * ValuePerMetrePrivate for i in UnitSizes]

"""OUTPUT WRITING"""
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
        if "A_" in Building[i][j]:
            sheet1.write((Levels + 1) - i, j + 1, Building[i][j],
                         xlwt.Style.easyxf(fmt_af))
        else :
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
OutputDirectory = "C:\\Users\\CN14439\\PycharmProjects\\MTD\\MTD_A_output\\"
OutputXLName = OutputDirectory + "output.xls"
book.save(OutputXLName)
