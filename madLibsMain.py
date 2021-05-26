from madLibsSets import holiday
from madLibsSets import theFunPark

print("Welcome to the Mad libs python game!")
print("Enter the word that matches the requirements.")

while True:
    setSelection = input("Select which Mad Libs set you would like to use?\n")
    if setSelection.lower() == "holiday":
        holiday()
        break
    elif setSelection.lower() == "the fun park":
        theFunPark()
        break