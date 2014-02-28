# Example code to use the library
from lib.wand import wand # Import library

wand.load(0.1) #Load GPIOs . Parameter is delay between LED line

wand.writeString('0123456789') # This will play when tilt switch / button creates circuit

wand.writeString('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') 




