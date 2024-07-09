'''
Program to automate agent select in Valorant Game.
'''

import pyautogui as pag
import keyboard as kb
import random
import tkinter as tk
from time import sleep

# Mouse Locations For Agent Selection

lock_in     =   (960,732)

astra       =   (626,840)
breach		=	(707,845)
brimstone	=	(797,843)
chamber		=	(875,841)
clove		=	(953,843)
cypher		=	(1037,837)
deadlock	=	(1130,842)
fade		=	(1223,840)
gekko		=	(1309,849)	
harbor		=	(624,926)
iso         =   (710,921)
jett		=	(794,924)
kayo		=	(875,930)
killjoy		=	(961,927)
neon		=	(1046,924)
omen		=	(1131,918)
phoenix		=	(1213,926)
raze		=	(1298,924)
reyna		=	(626,1014)
sage		=	(710,1015)
skye		=	(788,1017)
sova		=	(877,1015)
viper		=	(968,1011)
yoru		=	(1044,1014)

all_agents = [astra, breach, brimstone, chamber, clove, cypher, deadlock, fade, gekko, harbor, iso, jett, kayo, killjoy, neon, omen, phoenix, raze, reyna, sage, skye, sova, viper, yoru]

current_window = None

def switch_window(window_name):
    global current_window
    current_window = window_name


def In_Lock(Character):
    running = True
    sleep(3)
    while running:
        pag.leftClick(Character, _pause= False)
        sleep(0.01)
        pag.leftClick(lock_in, _pause= False)
        sleep(0.01)
        
        if kb.is_pressed('f6'):
            running = False


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def randomize_agent():
    running = True
    sleep(3)
    while running:
        selected_agent = random.choice(all_agents)
        pag.leftClick(selected_agent, _pause= False)
        sleep(0.01)

        while kb.is_pressed('f6'):
            pag.leftClick(lock_in, _pause= False)
            running = False
        
       

def randomizer_screen():
    clear_screen()
    switch_window('randomizer_screen')
    Home = tk.Button(root, text= "Home", command= main_window, height= 3, width= 10, bg='green', fg='white')
    Home.pack()
    root.geometry("300x250")
    
    randomize = tk.Button(root, text= "Randomize", command= randomize_agent, height= 5, width= 20)
    randomize.pack()
    


def agent_instalocker_screen():
    clear_screen()
    switch_window('Insta-Locker')
    Home = tk.Button(root, text= "Home", command= main_window, height= 3, width= 10, bg='green', fg='white')
    Home.grid(row= 0, column= 4, pady= 50)

    Astra = tk.Button(root,
                      text="Astra",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(astra))
    
    Breach = tk.Button(root,
                      text="Breach",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(breach))
    
    Brimstone = tk.Button(root,
                      text="Brimstone",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(brimstone))
    
    Chamber = tk.Button(root,
                      text="Chamber",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(chamber))
    
    Clove = tk.Button(root,
                      text="Clove",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(clove))
    
    Cypher = tk.Button(root,
                      text="Cypher",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(cypher))
    
    Deadlock = tk.Button(root,
                      text="Deadlock",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(deadlock))
    
    Fade = tk.Button(root,
                      text="Fade",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(fade))
    
    Gekko = tk.Button(root,
                      text="Gekko",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(gekko))
    
    Harbor = tk.Button(root,
                      text="Harbor",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(harbor))
    
    Iso = tk.Button(root,
                      text="Iso",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(iso))
    
    Jett = tk.Button(root,
                      text="Jett",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(jett))
    
    Kayo = tk.Button(root,
                      text="KAY/O",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(kayo))
    
    Killjoy = tk.Button(root,
                      text="Killjoy",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(killjoy))
    
    Neon = tk.Button(root,
                      text="Neon",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(neon))
    
    Omen = tk.Button(root,
                      text="Omen",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(omen))
    
    Phoenix = tk.Button(root,
                      text="Phoenix",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(phoenix))
    
    Raze = tk.Button(root,
                      text="Raze",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(raze))
    
    Reyna = tk.Button(root,
                      text="Reyna",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(reyna))
    
    Sage = tk.Button(root,
                      text="Sage",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(sage))
    
    Skye = tk.Button(root,
                      text="Skye",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(skye))
    
    Sova = tk.Button(root,
                      text="Sova",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(sova))
    
    Viper = tk.Button(root,
                      text="Viper",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(viper))
    
    Yoru = tk.Button(root,
                      text="Yoru",
                      height= 3,
                      width= 8,
                      command=lambda: In_Lock(yoru))
    
    
    Astra.grid(row= 1,column= 0, padx= 5, pady= 6)
    
    Breach.grid(row= 1,column= 1, padx= 6, pady= 6)
    
    Brimstone.grid(row= 1,column= 2, padx= 6, pady= 6)
    
    Chamber.grid(row= 1,column= 3, padx= 6, pady= 6)
    
    Clove.grid(row= 1,column= 4, padx= 6, pady= 6)
    
    Cypher.grid(row= 1,column= 5, padx= 6, pady= 6)
    
    Deadlock.grid(row= 1,column= 6, padx= 6, pady= 6)
    
    Fade.grid(row= 1,column= 7, padx= 6, pady= 6)
    
    Gekko.grid(row= 1,column= 8, padx= 6, pady= 6)
    
    Harbor.grid(row= 2, column= 0, padx= 5, pady= 6)
    
    Iso.grid(row= 2, column= 1, padx= 6, pady= 6)
    
    Jett.grid(row= 2, column= 2, padx= 6, pady= 6)
    
    Kayo.grid(row= 2, column= 3, padx= 6, pady= 6)
    
    Killjoy.grid(row= 2, column= 4, padx= 6, pady= 6)
    
    Neon.grid(row= 2, column= 5, padx= 6, pady= 6)
    
    Omen.grid(row= 2, column= 6, padx= 6, pady= 6)
    
    Phoenix.grid(row= 2, column= 7, padx= 6, pady= 6)
    
    Raze.grid(row= 2, column= 8, padx= 6, pady= 6)
    
    Reyna.grid(row= 3, column= 0, padx= 5, pady= 6)
    
    Sage.grid(row= 3, column= 1, padx= 6, pady= 6)
    
    Skye.grid(row= 3, column= 2, padx= 6, pady= 6)
    
    Sova.grid(row= 3, column= 3, padx= 6, pady= 6)
    
    Viper.grid(row= 3, column= 4, padx= 6, pady= 6)
    
    Yoru.grid(row= 3, column= 5, padx= 6, pady= 6)

def main_window():
    clear_screen()
    switch_window('Main')
    Randomize = tk.Button(root, text= "Random", command= randomizer_screen, height=5, width=12, bg='lightYellow', font=('CountryBlueprint', 25))
    Randomize.pack(side="left", padx= 50)

    InstaLocker = tk.Button(root, text="Insta-locker", command= agent_instalocker_screen, height=5, width=12, bg='lightYellow', font=('CountryBlueprint', 25))
    InstaLocker.pack(side="right", padx= 50)
    
    root.geometry("700x375")


root = tk.Tk()
root.title("Valorant Agent Picker")

root.resizable(False,False)
root.configure(bg='lightGreen')

main_window()

root.mainloop()
















"""
Used to move mouse to a certain location on screen
"""
# pag.moveTo(lock_in)



# press() is used to press a key
# leftClick() for left click of the mouse





# label = tk.Label(root, text = 'valorant agent selector')
# # label = tk.Label(root, text = 'AutoPicker')
# label.pack()

# button = tk.Button(root, text= 'STOP!', width= 25, command= root.destroy)

# button.pack()




"""
Code Below launches an app that helps in finding the location of mouse on screen for further automation.
"""
# pag.mouseInfo()


"""
Code Below is used to check if a particular key is pressed or not
"""
# while True:
#     if kb.is_pressed('a'):
#         print('Key "a" is pressed')
        
#     elif  kb.is_pressed('s'):
#         print('Key "s" is pressed')