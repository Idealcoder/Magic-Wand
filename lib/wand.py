import time
import RPi.GPIO as GPIO
from lib.font import loadFont

class wand(): 
	#================================================  GLOBALS	 ===================================
	
	font = loadFont()
	delay = 0 #Delay per line when writing	

	#================================================= FUNCTIONS ====================================
	def writeByte(byte):
		i=0
		for b in  str(str(bin(byte))[2:])[::-1]:
			#[2:] is to remove 0b (python binary header) from str
			# [::-1] inverts byte direction. 
			gp.output(i,b)
			i+=1
		while i<8:
			gp.output(i,0)
			i+=1
 
	#Write individual character
	def writeChar(char):
		if char in wand.font:
			char = wand.font[char]
		else:
			char = wand.font['pacman']
		
		for byte in char:
			#Loop through byte
			wand.writeByte(byte)
			time.sleep(wand.delay)
	
	#Write string in sequence
	def writeString(string):
		wand.wait() # Wait for wand to be flicked
		for char in string:
			#Loop through each letter in string 
			wand.writeChar(char)
			wand.writeChar('pad') # 1 line spacing between each letter

	def wait():
		#Wait for wand to be flicked
		GPIO.mode(GPIO.BOARD)
		while (GPIO.input(5) == True):
			time.sleep(0.0001) #High polling rate 
		GPIO.mode(GPIO.BCM)

	def load(delay):
		wand.delay = delay

		gp.load() # Setup GPIO pins for use
		
		#Setup input
		GPIO.mode(GPIO.BOARD)
		GPIO.setup(5,GPIO.IN)
		GPIO.mode(GPIO.BOARD)
		
		wand.writeChar('pad') #switch all GPIO to Off

		
# GPIO wrapper for higher level access
class gp():
	#For different pin set-ups
	matrix = {}

	matrix[0] = 18	
	matrix[1] = 23 
	matrix[2] = 24 
	matrix[3] = 4
	matrix[4] = 22 
	matrix[5] = 27
	matrix[6] = 17 
	matrix[7] = 25 

	#Output pin
	def output(pin,b):
		if int(b) == 1:
			GPIO.output(gp.matrix[pin],True)
		else:	
			GPIO.output(gp.matrix[pin],False)
	
	#Initialize pins
	def load():
		GPIO.setmode(GPIO.BCM)
		i=0
		while (i < 8 ):
			GPIO.setup(gp.matrix[i],GPIO.OUT)
			i+=1


