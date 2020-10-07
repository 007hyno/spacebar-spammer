from pynput.keyboard import Controller, Key
import time
k=Controller()
def ass():
    k.press(Key.space)
    k.release(Key.space)
time.sleep(2.4)
print("wait")
x=0
while x<50:
        time.sleep(0.10)
        ass()
        x+=1
print ("yoo")                                                                                 
