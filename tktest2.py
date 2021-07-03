import tkinter as tk
import random
from scipy import signal

out = open('Classifier/labeltest1.csv','w')
out.write('Dog,Cat,College,Lab,Friends\n')

class Text:
    def __init__(self, parent):
        # variable storing text
        self.text = ' '
        # label displaying text
        self.label = tk.Label(parent,bg='black',fg='white',text="Start",width=40,height=10,font=("Helvetica",120))
        self.label.pack()
        # start the timer
        self.label.after(2000, self.loop)
    def loop(self):
	self.text="Ready"
        self.label.configure(text='%s'%self.text)
        # start the timer
        self.label.after(2000, self.refresh_label_test)

    def refresh_label_test(self):
	names=['Dog','Cat','College','Lab','Friends']
	n=random.randint(0,4)
	self.text=names[n]
	self.label.configure(text='%s' %self.text)
	self.label.configure(fg='red')
	array = signal.unit_impulse(5,idx=n,dtype=int)	
	out.write(str(array[0])+','+str(array[1])+','+str(array[2])+','+str(array[3])+','+str(array[4])+'\n')
	self.label.after(7000,self.refresh_label_Relax)

    def refresh_label_Relax(self):
	self.text='Relax'
        # display the new text
        self.label.configure(text="%s " % self.text,fg='white')
        self.label.after(4000,self.loop)
    


if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1600x900")
	t = Text(root)
	root.mainloop()
