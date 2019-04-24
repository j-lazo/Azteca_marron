# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:59:07 2015

@author: jorge
"""

from Tkinter import *
import PIL.Image

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    fp = open('mapa.jpeg')
    img = PIL.Image.open(fp)
    img.show()
    #self.button = Button(frame,text="QUIT", fg="red",command=frame.quit)
    #self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.ShowImg)
                         

    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print "Tkinter is easy to use!"
    edit.add_comand(label='Show Image',command=self.showImg)
    
  def ShowImg(self):
      
        fp = open('mapa.jpeg',"rb")
        img = PIL.Image.open(fp)
        img.show()        
                
        #load=PIL.Image.Open('mapa.jpeg')
        r#ender=ImageTk.PhotoImage(load)
        
        img=Label(self,image=render)
        img.image=render
        img.place(x=15,y=15)

root = Tk()
app = App(root)
root.geometry("100x100")
root.mainloop()