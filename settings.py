#settings and vars

from tkinter import Grid


GameWidth = 1080
GameHeight = 720

TopBarWidth = GameWidth
TopBarHeight = GameHeight * 0.15

SideBarWidth = GameWidth * 0.15
SideBarHeight = GameHeight

GameViewWidth = GameWidth - (GameWidth * 0.15)
GameViewHeight = GameHeight - (GameHeight * 0.15)

#background colors
BackgroundPrimaryColor = "black"
BackgroudSecondaryColor = "black"




#game settings
GridSize = 7
TotalCellCount = GridSize ** 2
MinesCount = (GridSize ** 2) // 4

