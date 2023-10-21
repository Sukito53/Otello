from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import numpy as np

my_matrix = np.zeros((10, 10), dtype=np.int8)
for i in [0, 9]:
    for j in range(10):
        my_matrix[i, j] = 9
        my_matrix[j, i] = 9
my_matrix[4, 4] = -1
my_matrix[4, 5] = 1
my_matrix[5, 4] = 1
my_matrix[5, 5] = -1

class UI(Tk):
    def __init__(self):
        super().__init__()

        self.set_value()
        self.create()
        
    def set_value(self):
        self.geometry("1000x700+500+50")

        self.x_axis = ['A','B','C','D','E','F','G','H']
        self.y_axis = ['1','2','3','4','5','6','7','8']
        self.btn = [['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','','']]
        
        self.image = Image.open("Empty.png")  
        self.Empty = ImageTk.PhotoImage(self.image)
        self.image = Image.open("nothing.png")  
        self.nothing = ImageTk.PhotoImage(self.image)
        self.image = Image.open("white.png")  
        self.white = ImageTk.PhotoImage(self.image)
        self.image = Image.open("black.png")  
        self.black = ImageTk.PhotoImage(self.image)
        self.image = Image.open("pre.png")  
        self.pre = ImageTk.PhotoImage(self.image)
        self.custom_font = ("Times New Roman", 24)

    def create(self):
        self.label = Label(self,image=self.nothing)
        self.label.grid(row=0,column=0,padx=5,pady=5)

        for i in range(8):#ABCD
            self.label = Label(self, text=self.x_axis[i],width=1,height=1,font=self.custom_font)
            self.label.grid(row=0,column=i+1)

        for i in range(8):#1234
            self.label = Label(self, text=self.y_axis[i],width=1,height=1,font=self.custom_font)
            self.label.grid(row=i+1,column=0)

        for i in range(8):
            for j in range(8):
                if my_matrix[i+1][j+1] == 0:
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.Empty)
                elif my_matrix[i+1][j+1] == -1:
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.white)
                elif my_matrix[i+1][j+1] == 1:
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.black)
                else :
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.pre,command=lambda i=i+1,j=j+1: do(i,j))
                self.btn[i][j].grid(row=i+1,column=j+1)

    def update(self):
        for i in range(8):
            for j in range(8):
                if my_matrix[i+1][j+1] == 0:
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.Empty)
                elif my_matrix[i+1][j+1] == -1:
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.white)
                elif my_matrix[i+1][j+1] == 1:
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.black)
                else :
                    self.btn[i][j] = Button(self, text='',width=72,height=72,image=self.pre,command=lambda i=i+1, j=j+1: do(i,j))
                self.btn[i][j].grid(row=i+1,column=j+1)

def do(i,j):
    '''
    def do() is a function that waiting for input without input
    meaning is = when the button is clicked this function will activate and function will update matrix
    after that you can use self.update() for update matrix from code to show in UI

    and this function need 2 arguments that is
    i = row
    j = col

    *** Use {self.update()} for show matrix in UI ***
    '''

if __name__ == "__main__":
    main = UI()
    main.mainloop()
    