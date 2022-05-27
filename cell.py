from cProfile import label
from cgitb import text
from tkinter import Button, Label
import random
import settings

class Cell:
    all = []
    cell_count_label = None
    cell_count = settings.TotalCellCount
    gameOver = False

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_button_object = None
        self.is_clicked = False
        self.is_flagged = False
        #self.is_flagged = is_flagged
        
        
        #append object to cell.all list
        Cell.all.append(self)

    def create_button_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            bg='grey'
        )


        #Left Click<Button-1>
        #Right Click <Button-3>
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_button_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells Left: {Cell.cell_count}",
            width = 12,
            height = 4,
            font=("", 15)
        )
        Cell.cell_count_label = label
        


    def left_click_action(self, event):
        if(self.gameOver):
            return
        if(self.is_clicked):
            return
        
        if self.is_flagged:
            return

        if self.is_mine:
            self.show_mine()
            
        else:
            if self.number_of_surrounding_mines == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()

        if(Cell.cell_count == settings.MinesCount):
            Cell.cell_count_label.configure(text=f"You won!")
            self.gameOver = True
            


    def right_click_action(self, event):
        if(self.gameOver):
            return
        if(self.is_clicked):
            return
        if not self.is_flagged:
            self.is_flagged = True
            self.cell_button_object.configure(bg="orange")
        else:
            self.is_flagged = False
            self.cell_button_object.configure(bg='grey')



    def get_cell_by_axis(self, x,y):
        #return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1, self.y -1),
            self.get_cell_by_axis(self.x -1, self.y),
            self.get_cell_by_axis(self.x -1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y -1),
            self.get_cell_by_axis(self.x +1, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y),
            self.get_cell_by_axis(self.x +1, self.y +1),
            self.get_cell_by_axis(self.x , self.y +1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def number_of_surrounding_mines(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter




    def show_cell(self):
        if not self.is_clicked:
            Cell.cell_count -= 1
            self.cell_button_object.configure(text=self.number_of_surrounding_mines)
            #replace text of cell count label with new counter after process current clicked cell
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text=f"Cells Left: {Cell.cell_count}")
        
        #mark the cell as clicked, dont count anymore
        self.is_clicked = True

        

    def show_mine(self):
        
        #stop game, tell play they lost, show red background?
        self.cell_button_object.configure(bg="red")
        Cell.cell_count_label.configure(text=f"Game Over")
        self.gameOver = True
    
    @staticmethod
    def randmonize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MinesCount            
            )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            





    def __repr__(self):
        return f"Cell({self.x}, {self.y})"


    