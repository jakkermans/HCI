import threading
import time

class HCIButtonBox:
    pressed = False

    def press(self):
        self.pressed = not(self.pressed)

    def isOn(self):
        return self.pressed

class MachineAI:
    def __init__(self, cb):
        self.controlbutton = cb

    def startBot(self):
        threading.Thread(target=self.pressButton).start()

    def pressButton(self):
        while controlbutton.isOn():
            time.sleep(2.0)
            controlbutton.press()
            print("Turning switch off")
            inp.inputLoop()

class HumanInputGetter:
    def __init__(self, cb, mai):
        self.controlbutton = cb
        self.machineai = mai

    def startInput(self):
        threading.Thread(target=self.inputLoop).start()

    def inputLoop(self):
        while not controlbutton.isOn():
            inp = input("Type B to press the button.")
            if inp == "B":
                controlbutton.press()
                print("Turning switch on")
            elif inp == "Q":
                break
        machineai.pressButton()



controlbutton = HCIButtonBox()
machineai = MachineAI(controlbutton)
inp = HumanInputGetter(controlbutton, machineai)
inp.startInput()
machineai.startBot()
