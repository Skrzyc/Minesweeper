#!/usr/bin/python
from tkinter import *
import game

def run_game(mode):
    game.main(mode)

def main():
            
    class Menu_Frame:
        def __init__(self, height, posy, color):

            self.height = height
            self.posy = posy
            self.color = color

            self.frame = Frame(root,
                               height=self.height,
                               width=350,
                               bg=self.color)

            self.frame.place(x=0, y=self.posy)

    class Menu_Button:
        def __init__(self, text, col, posy, mode, root):

            self.root = root
            
            self.bgcol = 'grey95'
            self.height = 2
            
            self.mode = mode
            self.text = text
            self.col = col
            self.posy = posy

            if self.mode == 66:
                self.bgcol = 'grey'
                self.height = 1

            self.btn = Button(root,
                              width = 25,
                              height = self.height,
                              relief = 'groove',
                              bg = self.bgcol,
                              fg = self.col,
                              font = 'Verdana 16',
                              text = self.text,
                              command=lambda: click(self.mode))

            self.btn.place(x=7, y=self.posy)

            def click(mode):
                if mode == 66: self.root.destroy()
                else:
                    self.root.destroy()
                    run_game(mode)
                
    


    root = Tk()
    root.title('Minesweeper - Menu')
    root.geometry('350x420')
    
    f1 = Menu_Frame(120,0,'white smoke')
    f2 = Menu_Frame(280,120,'grey94')
    
    f1 = Frame(root)

    label = Label(root, text='*** MINESWEEPER ***',
                  bg='white smoke',fg='orange2',
                  font='oemfixed 20 bold')

    label.place(x=30, y=40)

    Menu_Button('Easy','blue',130,0,root)
    Menu_Button('Medium','green',205,1,root)
    Menu_Button('Hard','red',280,2,root)
    Menu_Button('Quit','white',370,66,root)

    root.mainloop()


if __name__ == "__main__":
    main()







