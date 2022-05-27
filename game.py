#game from https://www.youtube.com/watch?v=OqbGRZx4xUc&t=1695s
#Minesweeper
#SeanLaing2022




from tkinter import *
import settings
from cell import Cell

#vars
width = 1080
height = 720


#Instatiate
root = Tk()


root.configure(bg=settings.BackgroundPrimaryColor)
root.geometry(f'{settings.GameWidth}x{settings.GameHeight}')
root.title('Minesweeper - Sean')
root.resizable(FALSE, FALSE)


#run the window
top_frame = Frame(
    root,
    bg=settings.BackgroundPrimaryColor, 
    width=settings.TopBarWidth,
    height=settings.TopBarHeight
    )

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper - Sean Laing',
    font=('',30)
)

game_title.place(
    x=settings.TopBarWidth * 0.25,y=settings.TopBarHeight * 0.10
)

left_frame = Frame(
    root,
    bg=settings.BackgroundPrimaryColor, 
    width=settings.SideBarWidth,
    height=settings.SideBarHeight
)
left_frame.place(x=0, y=settings.TopBarHeight)


game_frame = Frame(
    root,
    bg=settings.BackgroundPrimaryColor,
    width=settings.GameViewWidth,
    height=settings.GameViewHeight
)


game_frame.place(x=settings.SideBarWidth, y=settings.TopBarHeight)





#cells
for x in range(settings.GridSize):
    for y in range(settings.GridSize):
        c = Cell(x, y)
        c.create_button_object(game_frame)
        c.cell_button_object.grid(column=x, row=y)


#call the label from Cell class to show remaining cell count
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x = 0, y = 0)



Cell.randmonize_mines()
#Debug mine assignment
#for c in Cell.all:
#    print(c.is_mine)




#idk but window opens
root.mainloop()





