from html.entities import name2codepoint
from unicodedata import name
import pyautogui as auto
import time 
from py import process
import sys 

def play_a_song(name):
    # auto.click(x=541, y=865) #opens spotify
    auto.hotkey('command','space') 
    auto.write("spotify")
    auto.press("enter")
    time.sleep(1)
    auto.click(x=55,y=78) #va dans la barre chercher 
    auto.click(x=704, y=31)
    auto.write(name)
    auto.press("enter")
    time.sleep(1)
    auto.click(x=746,y=158)
    process.exit(1)
if __name__=="__main__":
    name_of_song = ""
    for i in range(1,len(sys.argv)):
        name_of_song += sys.argv[i] + " "
    print("looking for", name_of_song)
    play_a_song(name_of_song)

