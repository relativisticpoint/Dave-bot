import pyautogui as dave
import time 
import sys 

def play_a_song(name):
    dave.hotkey('command','space') #opens the spotlight search to look for the spotify app
    dave.write("spotify")
    dave.press("enter")
    time.sleep(1)
    dave.hotkey('command','l') #uses the default spotify search shortcut
    dave.write(name)
    time.sleep(1)
    dave.press("enter")
    # dave.click(x=746,y=158) #clicks on the first recommended song
    for i in range(3):
        dave.press("tab")
    dave.press("enter")
    return
    
if __name__=="__main__":
    name_of_song = ""
    for i in range(1,len(sys.argv)):
        name_of_song += sys.argv[i] + " "
    print("Launching Spotify and playing ", name_of_song)
    play_a_song(name_of_song)

