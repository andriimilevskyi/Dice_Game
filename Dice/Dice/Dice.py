from pydoc import plain
from random import *
from tkinter import *
from  tkinter import ttk
import random



player1 = 0
player2 = 0

def Roll_TwoDice():
   global dice1
   global dice2
   dice1 = random.randint(1,6)
   dice2 = random.randint(1,6)
   #return dice1,dice2

   
def Run_Game():
    global score1
    Roll_TwoDice()
    score1 = []
    score1.append(dice1)

def main():
    Run_Game()
    print(score1)

main()

window = Tk()

window.title("Dice Round")
window.geometry('600x400')
window['bg'] = 'lightgray'
game_frame = Frame(window)
game_frame.pack()

game_table = ttk.Treeview(game_frame)
game_table['columns'] = ('player_num', 'first', 'second', 'third', 'result')

game_table.column("#0", width=0,  stretch=NO)
game_table.column("player_num",anchor=CENTER, width=80)
game_table.column("first",anchor=CENTER,width=80)
game_table.column("second",anchor=CENTER,width=80)
game_table.column("third",anchor=CENTER,width=80)
game_table.column("result",anchor=CENTER,width=80)

#game_table.heading("#0",text="",anchor=CENTER)
#game_table.heading("player_num",text="Id",anchor=CENTER)
#game_table.heading("first",text="Name",anchor=CENTER)
#game_table.heading("second",text="Rank",anchor=CENTER)
#game_table.heading("third",text="States",anchor=CENTER)
#game_table.heading("result",text="States",anchor=CENTER)


#def clicked():
    
#btn = Button(window, text="Click Me")

game_table.insert(parent='',index='end',iid=0,text='',
values=('Player1','',score1[0],'3', 'res2'))
game_table.insert(parent='',index='end',iid=1,text='',
values=('Player2','1','2','3', 'res2'))


game_table.pack()


window.mainloop()


    
    #player1 += dice1 + dice2




