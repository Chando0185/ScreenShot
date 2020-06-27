import pyautogui
from tkinter import *
import time
import random

result=random.randint(1,100010)

root=Tk()
root.title("ScreenShot GUI")
root.geometry("250x300")

l1=Label(root,text="ScreenShot GUI",font="times 20 bold")
l1.pack()

def shot():
	root.withdraw()
	time.sleep(3)
	img=pyautogui.screenshot()
	img.save(f"screenshot{result}.jpg")


btn=Button(root,text="Click",command=shot)
btn.pack()

root.mainloop()