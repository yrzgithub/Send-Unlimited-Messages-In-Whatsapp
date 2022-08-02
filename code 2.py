import keyboard
import time

msg = "Hello"
num = 1

print("Waiting for shift..")
keyboard.wait("shift")
print("Press ctrl to stop...")

while not keyboard.is_pressed("ctrl"):
    to_print = f"{num}.{msg}"
    keyboard.write(to_print)
    time.sleep(0.1)
    keyboard.press_and_release("enter")
    time.sleep(0.1)
    num+=1

print("Loop stopped..")
print("Messages sent...")
