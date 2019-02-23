from tkinter import *
from comb2br import *
from tkinter import messagebox
import os
import re
from keras import backend as K
from threading import Thread

oc = -1    
selected = None

def clked2():
    class MyTrd3(Thread):
        def run(self):
            window.update()
            global oc
            nc = int(selected.get())
            if nc != oc:
                count,ic,obj = open_cam(nc)
                messagebox.showinfo("No of persons","No of person %d\nAverage person per frame %d" %(count,count/ic))
        K.clear_session()
    t3 = MyTrd3()
    t3.start()

        
def clicked():
    class MyTrd2(Thread):
        def run(self):
            window.update()
            global selected
            selected = IntVar()
            selected.set(-1)
            camop = get_cam()
            r = 4
            for k1 in camop:
                rad1 = Radiobutton(window, text=k1, value=camop[k1], variable=selected, font=("jokerman", 20), command=clked2)
                rad1.grid(column=0, row=r, sticky=W+E+N+S, padx=5, pady=20)
                r = r + 1
    t2 = MyTrd2()
    t2.start()
        
def clicked3():
    class MyTrd1(Thread):
         def run(self):
            window.update()
            from tkinter.filedialog import askopenfilename
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filename = askopenfilename() # show an "Open" dialog box and return the path to the selected 
            print("filename ======== %s" %filename)
            if len(filename) == 0:
                None
            else:
                count,ic,obj = browse(filename)
                messagebox.showinfo("No of persons","No of person %d\nAverage person per frame %d" %(count,count/ic))
            K.clear_session()
    t1 = MyTrd1()
    t1.start()
def clicked4():
    window.update()
    os.startfile(r"img") 
def clicked5():
    window.update()
    os.startfile(r"countexcel")

# print("Made by- ABHIJEET PANSARI")
window = Tk()
window.title(" AI ")
lbl = Label(window, text=" OBJECT DETECTOR ",  bg="black", fg="white", font=("jokerman", 40))
lbl.pack(expand=YES, fill=BOTH)
lbl.grid(column=0, row = 0)
btn = Button(window, text="Search Cameras", font=("jokerman", 20), command=clicked)
btn.grid(column=0, row=4,  sticky=W+E+N+S, padx=5, pady=20)
btn = Button(window, text="Browse", font=("jokerman", 20), command=clicked3)
btn.grid(column=0, row=3,  sticky=W+E+N+S, padx=5, pady=20)
btn = Button(window, text="Saved Images", font=("jokerman", 20), command=clicked4)
btn.grid(column=0, row=1,  sticky=W+E+N+S, padx=5, pady=20)
btn = Button(window, text="Previous Records", font=("jokerman", 20), command=clicked5)
btn.grid(column=0, row=2,  sticky=W+E+N+S, padx=5, pady=20)
window.mainloop()


