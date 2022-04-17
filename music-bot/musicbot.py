from html.entities import name2codepoint
from unicodedata import name
import pyautogui as auto
import time 
from py import process
import sys 

def play_a_song(name):
    auto.hotkey('command','space') #opens the spotlight search to look for the spotify app
    auto.write("spotify")
    auto.press("enter")
    time.sleep(1)
    auto.click(x=55,y=78) # goes to the search bar
    auto.click(x=704, y=31) #clicks on the cross to delete any previous search in the search bar
    auto.write(name)
    auto.press("enter")
    time.sleep(1)
    auto.click(x=746,y=158) #clicks on the first recommended song
    return
if __name__=="__main__":
    name_of_song = ""
    for i in range(1,len(sys.argv)):
        name_of_song += sys.argv[i] + " "
    print("Launching Spotify and playing ", name_of_song)
    play_a_song(name_of_song)

