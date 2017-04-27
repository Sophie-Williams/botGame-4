import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from grabscreen import grab_screen
from directkeys import PressKey, ReleaseKey, W, A, S, D

def up():
	PressKey(W)
	time.sleep(0.2)
	ReleaseKey(W)

def left():
	PressKey(A)
	time.sleep(0.1)
	ReleaseKey(A)

def right():
	PressKey(D)
	time.sleep(0.1)
	ReleaseKey(D)
	
def down():
	PressKey(S)
	time.sleep(0.2) #increasing the time of sleep will increase speed at which player moves
	ReleaseKey(S)

def jumpLeft():
	PressKey(W)
	PressKey(A)
	time.sleep(0.25)
	ReleaseKey(A)
	ReleaseKey(W)

def jumpRight():	
	PressKey(W)
	PressKey(D)
	time.sleep(0.25) #this needs to be modified so that player can jump the bigger platforms after eating the shroom
	ReleaseKey(D)
	ReleaseKey(W)
	
def main():
	for i in list(range(4))[::-1]:
		time.sleep(1)
	
	while True:
		screen = grab_screen(region=(6,126,526,646)) #use paint to get this?
		#screen =  np.array(ImageGrab.grab(bbox=(0,120,550,550)))
		#screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
		screen = cv2.resize(screen, (84,84))
		cv2.imshow('window', screen)
		cv2.moveWindow('window',700, 0)
		left()
		
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

main()