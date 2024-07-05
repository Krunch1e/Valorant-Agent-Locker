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


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def randomize_agent():
    # Wait for F6 key press to start
    while not kb.is_pressed('f6'):
        sleep(0.0001)  # Short delay to avoid overwhelming CPU

    # Random selection loop
    while True:
        selected_agent = random.choice(all_agents)
        pag.moveTo(selected_agent)

        # Check if F1 is pressed to lock in
        if kb.is_pressed('f6'):
            pag.moveTo(lock_in)
            break



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
    Home.pack()


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