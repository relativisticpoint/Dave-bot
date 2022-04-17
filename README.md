# Python-Bot
Dave is a bot that opens spotify and plays the song it is given as a parameter using the pyautogui library.
## How it works
Execute the script passing the name of the song you want to listen to as a parameter. 
``` 
$ python3 musicbot.py <name_of_the_song> 
```
For example :
```
$ python3 musicbot.py highway to hell
```
## Additional info
Dave was coded using the PyAutoGUI Library that lets your Python scripts control the mouse and keyboard to automate interactions with other applications. It uses keyboard shortcuts to find spotify, go to the search bar...

The delay between two successive commands executed is set to 1 second, it can be changed from the script if the delay of the connection is longer. by changing this line :
```
time.sleep(1) #can be changed to a delay that suits the user
```
The pyautoui api is simple and intuitive to use, and the script runs on both **Python 2 and 3 versions**
## Limitations
- For now the Dave bot only works on MacOS since it uses specific MacOS shortcuts, an upcomming version would include Windows and Linux OS systems as well.
