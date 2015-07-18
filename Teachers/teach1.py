from Tkinter import *
#from teach2 import x

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.slogan = Button(frame,
                         text="Submit",
                         command=self.write_file)
    self.slogan.pack(side=BOTTOM)
  def write_file(self):
  	x = open("ans.txt","w")
	thetext = T.get('1.0', 'end')
	x.write(thetext)
	x.close()
	root.destroy()
root = Tk()
root.wm_title("Model Answer")
T = Text(root, height=30, width=120)
T.pack()
app = App(root)
root.mainloop()
x = raw_input("Enter the keywords seperated by commas:\n>")
xyz = [str(a) for a in x.split(" ")]
f1 = open("key.txt",'w')
f1.write(xyz[0])
f1.close()

