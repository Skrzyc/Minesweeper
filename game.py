#!/usr/bin/python
try:                        
    from tkinter import *   
    from tkinter import messagebox 
except:
    from Tkinter import *
    from Tkinter import messagebox
from math import fabs
from random import randint

def create_map(tab):

    def make_mine():
        return randint(0,tab[1]*tab[0])
    
    tabxy = []
    mines = []
    
    for x in range(0,tab[2]):
        
        m = make_mine()
        while True:
            if m in mines:
                m = make_mine()
            else:
                break
            
        mines.append(m)
        
    for x in range(0,tab[0]*tab[1]+1): #empty list
        tabxy.append(0)
    
    for x in range(0,tab[0]*tab[1]+1): #list with mines
        if x in mines:
            tabxy[x] = 100
      
    for x in range(0,len(mines)):           #list with mines and numbers
        for y in range(1,(tab[0]*tab[1])+1):
            
            if mines[x]%tab[0] == 0:                    #for the first column
                if mines[x]-y == 1: tabxy[y] += 1
                if mines[x]-y+tab[0] == 1 or mines[x]-y+tab[0] == 0: tabxy[y] += 1
                if mines[x]-y-tab[0] == 1 or mines[x]-y-tab[0] == 0: tabxy[y] += 1
            elif mines[x]%tab[0] == 1:                  #for the last column
                if y-mines[x] == 1: tabxy[y] += 1
                if y-mines[x]+tab[0] == 1 or y-mines[x]+tab[0] == 0: tabxy[y] += 1
                if y-mines[x]-tab[0] == 1 or y-mines[x]-tab[0] == 0: tabxy[y] += 1
            else:                                       #for the rest 
                if fabs(mines[x]-y) <= 1: tabxy[y] += 1        
                if fabs(mines[x]-y+tab[0]) <= 1: tabxy[y] += 1 
                if fabs(mines[x]-y-tab[0]) <= 1: tabxy[y] += 1 
    
    return tabxy


def main(mode):
        
    class Btn:
        def __init__(self,row,col):

            self.val = 0        
            self.color = 'snow3' 
            self.bgcolor = 'snow3'
            
            self.row = row      
            self.col = col  
                
            def click():
                self.btn = Button(root,
                                  state='normal',
                                  text=' '+str(self.val)+' ',
                                  bg=self.bgcolor,
                                  fg=self.color)
                
                self.btn.grid(row=row,column=col) 
                
            self.btn = Button(root, text=' ',padx=8, pady=4, command=click)
            self.btn.grid(row=row,column=col)


    class Mine:
        def __init__(self, row, col,root):

            self.root = root
            self.row = row
            self.col = col
            
            self.color = 'black'
            self.val = 'M'
            self.bgcolor = 'red'

            def click_mine():
                self.btn = Button(root,
                                  state='normal',
                                  text=' M ',
                                  bg='red',
                                  fg='black')
                explode()
                
            self.btn = Button(root, text=' ',padx=8, pady=4, command=click_mine)
            self.btn.grid(row=self.row, column=col)
            
            def explode():
                messagebox.showinfo('Lost Game','You Exploded !!!')
                self.root.destroy()
            

    class Btn1(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'blue'
            self.val = 1

    class Btn2(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'green'
            self.val = 2

    class Btn3(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'red'
            self.val = 3

    class Btn4(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'navy'
            self.val = 4

    class Btn5(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'firebrick4'
            self.val = 5

    class Btn6(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'dodger blue'
            self.val = 6

    class Btn7(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'black'
            self.val = 7

    class Btn8(Btn):
        def __init__(self, row, col):
            super().__init__(row, col)
            self.color = 'gray35'
            self.val = 8
    
    root = Tk()
    root.title('Minesweeper')
    tab = []
    
    if mode == 0:
        tab = (8,8,10)
    elif mode == 1:
        tab = (12, 12, 30)
    elif mode == 2:
        tab = (16, 16, 50)

    tabxy = create_map(tab)
    
    y = 0
    m = 0
    for x in range(1,len(tabxy)):
        
        m = x - y*tab[0]   
        if tabxy[x] > 99:
            Mine(y,m,root)
        elif tabxy[x] == 1:
            Btn1(y,m)
        elif tabxy[x] == 2:
            Btn2(y,m)
        elif tabxy[x] == 3:
            Btn3(y,m)
        elif tabxy[x] == 4:
            Btn4(y,m)
        elif tabxy[x] == 5:
            Btn5(y,m)
        elif tabxy[x] == 6:
            Btn6(y,m)
        elif tabxy[x] == 7:
            Btn7(y,m)
        elif tabxy[x] == 8:
            Btn8(y,m)
        else:
            Btn(y,m)
        
        if x == 0:
            pass
        else:
            if x%tab[0] == 0: y = y + 1
            

#main(0)
# mines left
# if clicks = tab[0]*tab[1]-len(mines) -> WIN

# może się uda zrobić te pola szare z pierwszym przyciskiem
# może się uda zrobić też że te pola szare odkrywają same jeżeli się nacisnie

#   przycik obok szarych pól

# skimń czy niektórych elementów nie dałoby radey napisać łatwiej

# popraw stylistyke
# comments popraw
