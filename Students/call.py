from try2 import main
from Tkinter import *


class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.slogan = Button(frame,
                         text="Submit",
                         command=self.write_file)
    self.slogan.pack(side=BOTTOM)
  def write_file(self):
  	x = open("new.txt","w")
	thetext = T.get('1.0', 'end')
	x.write(thetext)
	x.close()
	root.destroy()
	main()
root = Tk()
root.wm_title("Unbiased Exam Checker")
T = Text(root, height=30, width=120)
T.pack()
app = App(root)
root.mainloop()

