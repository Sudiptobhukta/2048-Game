from cProfile import label
from tkinter import Frame, Label,CENTER
import logic
import constants as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self) 
        #'''this define or give a skeleton/Frame skeleton of the window that
        # we are calling a Frame'''


        self.grid() #this forms the grid inside the Frame that we just made 🔼above
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands = {c.KEY_UP: logic.move_up, c.KEY_DOWN: logic.move_down,
                          c.KEY_LEFT: logic.move_left, c.KEY_RIGHT: logic.move_right}
        self.grid_cell =[]
        self.init_grid()
        self.init_matrix()
        self.updated_grid_cell()

        self.mainloop() 
        #this method tells the tkinter to run, this method listens to the events such as botton press, keypress and any movements in the keyboard

    def init_grid(self):
        background = Frame(self,bg=c.BACKGROUND_COLOR_GAME, 
                            width=c.SIZE, height=c.SIZE)
        

        background.grid()

        for i in range(c.GRID_LEN):
            grid_row=[]    
            for j in range(c.GRID_LEN):
                cell = Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY, 
                              width=c.SIZE/c.GRID_LEN, 
                              height= c.SIZE/c.GRID_LEN)

                ''' we wrote "background" inside the frame because this tells that we are building 
                the cells inside the background frame'''

                cell.grid(row=i,column=j, padx=c.GRID_PADDING,
                           pady=c.GRID_PADDING)
                          
                t= Label(master=cell, text="", justify=CENTER, 
                           font= c.FONT, width=5,
                           height=2)

                t.grid()
                grid_row.append(t)

            self.grid_cell.append(grid_row)

    
    def init_matrix(self):
        self.matrix = logic.Start_Game()
        logic.Random_2(self.matrix)
        logic.Random_2(self.matrix)

    def updated_grid_cell(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number ==0:
                    self.grid_cell[i][j].configure(text=" ", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                
                else:
                    self.grid_cell[i][j].configure(text=str(new_number),bg = c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks() #this function will make the updated_grid_cell wait untill all the cells and colour are changed

    def key_down(self,event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix,flag = self.commands[repr(event.char)](self.matrix)
            if flag:
                logic.Random_2(self.matrix)
                self.updated_grid_cell()
                flag= False
                if logic.Status(self.matrix)=='WON':
                    self.grid_cell[1][1].configure(text="YOU", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cell[1][2].configure(text="WIN!", bg = c.BACKGROUND_COLOR_CELL_EMPTY)

                if logic.Status(self.matrix)=='LOST':
                    self.grid_cell[1][1].configure(text="YOU", bg= c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cell[1][2].configure(text='LOSE!', bg=c.BACKGROUND_COLOR_CELL_EMPTY)

gamegrid=Game2048()